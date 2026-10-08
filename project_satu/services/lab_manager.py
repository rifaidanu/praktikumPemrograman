from datetime import date, datetime
from typing import Dict, List, Optional, Set

from models.enums import KondisiAlat, StatusAlat, StatusTransaksi
from models.mahasiswa import Mahasiswa
from models.peralatan import Peralatan
from models.transaksi import ItemPeminjaman, Transaksi


class LabManager:
    """Pusat data dan pengatur logika bisnis sistem laboratorium."""

    def __init__(self) -> None:
        self._mahasiswa: Dict[str, Mahasiswa] = {}   # nim -> Mahasiswa
        self._alat: Dict[str, Peralatan] = {}        # kode_alat -> Peralatan
        self._transaksi: Dict[str, Transaksi] = {}   # id_transaksi -> Transaksi
        self._kategori: Set[str] = set()
        self._log: List[dict] = []

    # ==================== PROPERTIES ====================
    @property
    def mahasiswa(self) -> Dict[str, Mahasiswa]:
        return self._mahasiswa

    @property
    def alat(self) -> Dict[str, Peralatan]:
        return self._alat

    @property
    def transaksi(self) -> Dict[str, Transaksi]:
        return self._transaksi

    @property
    def kategori(self) -> Set[str]:
        return self._kategori

    @property
    def log(self) -> List[dict]:
        return self._log

    # ==================== LOGGING ====================
    def catat_log(self, pesan: str) -> None:
        """Mencatat aktivitas ke dalam list log."""
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._log.append({"waktu": waktu, "pesan": pesan})

    # ==================== KELOLA MAHASISWA ====================
    def tambah_mahasiswa(self, nim: str, nama: str, nomor_hp: str) -> Mahasiswa:
        if nim in self._mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM '{nim}' sudah terdaftar.")
        mhs = Mahasiswa(nim, nama, nomor_hp)
        self._mahasiswa[nim] = mhs
        self.catat_log(f"Tambah mahasiswa: {nim} - {nama}")
        return mhs

    def edit_mahasiswa(self, nim: str, nama: Optional[str] = None, nomor_hp: Optional[str] = None) -> Mahasiswa:
        if nim not in self._mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        mhs = self._mahasiswa[nim]
        if nama is not None and nama.strip():
            mhs.nama = nama
        if nomor_hp is not None and nomor_hp.strip():
            mhs.nomor_hp = nomor_hp
        self.catat_log(f"Edit mahasiswa: {nim}")
        return mhs

    def hapus_mahasiswa(self, nim: str) -> None:
        if nim not in self._mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        mhs = self._mahasiswa[nim]
        if mhs.punya_peminjaman_aktif():
            raise ValueError("Tidak dapat menghapus: Mahasiswa masih memiliki transaksi peminjaman aktif.")
        del self._mahasiswa[nim]
        self.catat_log(f"Hapus mahasiswa: {nim}")

    def cari_mahasiswa(self, keyword: str) -> List[Mahasiswa]:
        keyword = keyword.lower()
        return [
            m for m in self._mahasiswa.values()
            if keyword in m.nim.lower() or keyword in m.nama.lower()
        ]

    # ==================== KELOLA ALAT ====================
    def tambah_kategori(self, nama_kategori: str) -> None:
        kat = nama_kategori.strip()
        if kat:
            self._kategori.add(kat)

    def tambah_alat(
        self,
        kode_alat: str,
        nama: str,
        kategori: str,
        kondisi: KondisiAlat = KondisiAlat.BAIK
    ) -> Peralatan:
        if kode_alat in self._alat:
            raise ValueError(f"Alat dengan kode '{kode_alat}' sudah terdaftar.")
        self.tambah_kategori(kategori)
        unit = Peralatan(kode_alat, nama, kategori, kondisi)
        self._alat[kode_alat] = unit
        self.catat_log(f"Tambah alat: {kode_alat} - {nama} ({kategori})")
        return unit

    def edit_alat(
        self,
        kode_alat: str,
        nama: Optional[str] = None,
        kategori: Optional[str] = None,
        kondisi: Optional[KondisiAlat] = None
    ) -> Peralatan:
        if kode_alat not in self._alat:
            raise ValueError(f"Alat dengan kode '{kode_alat}' tidak ditemukan.")
        unit = self._alat[kode_alat]
        if nama is not None and nama.strip():
            unit.nama = nama
        if kategori is not None and kategori.strip():
            unit.kategori = kategori
            self.tambah_kategori(kategori)
        if kondisi is not None:
            unit.kondisi = kondisi
            if not unit.sedang_dipinjam():
                unit.status = StatusAlat.TERSEDIA if kondisi == KondisiAlat.BAIK else StatusAlat.TIDAK_TERSEDIA
        self.catat_log(f"Edit alat: {kode_alat}")
        return unit

    def hapus_alat(self, kode_alat: str) -> None:
        if kode_alat not in self._alat:
            raise ValueError(f"Alat dengan kode '{kode_alat}' tidak ditemukan.")
        if self._alat_dipakai_transaksi_aktif(kode_alat):
            raise ValueError("Tidak dapat menghapus: Alat masih tercatat dalam transaksi yang sedang aktif.")
        del self._alat[kode_alat]
        self.catat_log(f"Hapus alat: {kode_alat}")

    def cari_alat(self, keyword: str) -> List[Peralatan]:
        keyword = keyword.lower()
        return [
            a for a in self._alat.values()
            if keyword in a.kode_alat.lower() or keyword in a.nama.lower() or keyword in a.kategori.lower()
        ]

    def _alat_dipakai_transaksi_aktif(self, kode_alat: str) -> bool:
        """Memeriksa apakah alat masih ada di dalam transaksi yang belum selesai."""
        for t in self._transaksi.values():
            if t.masih_aktif():
                for item in t.daftar_item:
                    if item.alat.kode_alat == kode_alat:
                        return True
        return False

    # ==================== KELOLA TRANSAKSI ====================
    def buat_transaksi(self, nim: str, daftar_kode_alat: List[str], batas: date) -> Transaksi:
        # --- Fase 1: Validasi (tanpa mengubah data apa pun) ---
        if nim not in self._mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        mhs = self._mahasiswa[nim]
        if not mhs.boleh_meminjam():
            raise ValueError(f"Mahasiswa '{mhs.nama}' sudah mencapai batas maksimal {Mahasiswa.MAKS_TRANSAKSI_AKTIF} transaksi aktif.")
        if not daftar_kode_alat:
            raise ValueError("Daftar alat tidak boleh kosong.")

        for kode in daftar_kode_alat:
            if kode not in self._alat:
                raise ValueError(f"Alat dengan kode '{kode}' tidak ditemukan.")
            if not self._alat[kode].tersedia():
                raise ValueError(f"Alat '{self._alat[kode].nama}' ({kode}) tidak tersedia untuk dipinjam (Status: {self._alat[kode].status.value}).")

        # --- Fase 2: Eksekusi Perubahan Data ---
        items = [ItemPeminjaman(self._alat[k]) for k in daftar_kode_alat]
        id_baru = f"T{len(self._transaksi) + 1:03d}"
        transaksi = Transaksi(id_baru, mhs, items, date.today(), batas)

        if not transaksi.validasi_batas():
            raise ValueError("Batas pengembalian tidak valid (maksimal 7 hari dari hari ini).")

        for item in items:
            item.alat.tandai_dipinjam()

        mhs.tambah_transaksi_aktif(transaksi)
        self._transaksi[id_baru] = transaksi
        self.catat_log(f"Buat transaksi {id_baru} untuk NIM {nim} ({len(items)} alat)")
        return transaksi

    def proses_pengembalian(self, id_transaksi: str, kode_alat: str, kondisi: KondisiAlat) -> Transaksi:
        if id_transaksi not in self._transaksi:
            raise ValueError(f"Transaksi dengan ID '{id_transaksi}' tidak ditemukan.")
        transaksi = self._transaksi[id_transaksi]
        if not transaksi.masih_aktif():
            raise ValueError(f"Transaksi '{id_transaksi}' sudah berstatus SELESAI.")

        transaksi.kembalikan_alat(kode_alat, kondisi, date.today())
        self.catat_log(f"Pengembalian alat {kode_alat} pada transaksi {id_transaksi} (Kondisi: {kondisi.value})")
        return transaksi

    def tampilkan_transaksi(self) -> List[Transaksi]:
        """Mengembalikan semua transaksi yang tercatat."""
        return list(self._transaksi.values())

    def cari_transaksi_by_mahasiswa(self, nim: str) -> List[Transaksi]:
        """Mencari transaksi aktif maupun selesai milik mahasiswa tertentu."""
        return [t for t in self._transaksi.values() if t.mahasiswa.nim == nim]

    def riwayat_mahasiswa(self, nim: str) -> List[Transaksi]:
        """Alias / fungsi untuk melihat seluruh riwayat peminjaman mahasiswa."""
        if nim not in self._mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        return self.cari_transaksi_by_mahasiswa(nim)

    # ==================== TAMPILAN & FILTER ALAT ====================
    def tampilkan_alat_tersedia(self) -> List[Peralatan]:
        return [a for a in self._alat.values() if a.status == StatusAlat.TERSEDIA]

    def tampilkan_alat_dipinjam(self) -> List[Peralatan]:
        return [a for a in self._alat.values() if a.status == StatusAlat.DIPINJAM]

    def tampilkan_alat_rusak(self) -> List[Peralatan]:
        return [
            a for a in self._alat.values()
            if a.kondisi in (KondisiAlat.RUSAK_RINGAN, KondisiAlat.RUSAK_BERAT)
        ]
