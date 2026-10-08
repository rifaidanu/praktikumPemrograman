from datetime import date, timedelta
from typing import List, Optional

from .enums import KondisiAlat, StatusTransaksi
from .mahasiswa import Mahasiswa
from .peralatan import Peralatan


class ItemPeminjaman:
    """Mewakili satu baris/item alat di dalam transaksi peminjaman."""

    def __init__(self, alat: Peralatan) -> None:
        self._alat: Peralatan = alat
        self._sudah_kembali: bool = False
        self._tanggal_kembali: Optional[date] = None
        self._kondisi_kembali: Optional[KondisiAlat] = None

    @property
    def alat(self) -> Peralatan:
        return self._alat

    @property
    def sudah_kembali(self) -> bool:
        return self._sudah_kembali

    @property
    def tanggal_kembali(self) -> Optional[date]:
        return self._tanggal_kembali

    @property
    def kondisi_kembali(self) -> Optional[KondisiAlat]:
        return self._kondisi_kembali

    def tandai_kembali(self, kondisi: KondisiAlat, tanggal: date) -> None:
        """Menandai bahwa alat ini sudah dikembalikan dan memperbarui status unit alatnya."""
        self._sudah_kembali = True
        self._tanggal_kembali = tanggal
        self._kondisi_kembali = kondisi
        self._alat.terima_kembali(kondisi)

    def __repr__(self) -> str:
        status_str = f"Kembali ({self._kondisi_kembali.value if self._kondisi_kembali else '-'})" if self._sudah_kembali else "Dipinjam"
        return f"<Item {self._alat.kode_alat} ({self._alat.nama}): {status_str}>"


class Transaksi:
    """Mewakili satu transaksi peminjaman yang dapat memuat banyak item alat."""
    MAKS_HARI: int = 7

    def __init__(
        self,
        id_transaksi: str,
        mahasiswa: Mahasiswa,
        daftar_item: List[ItemPeminjaman],
        tanggal_peminjaman: date,
        batas_pengembalian: date
    ) -> None:
        self._id_transaksi: str = id_transaksi
        self._mahasiswa: Mahasiswa = mahasiswa
        self._daftar_item: List[ItemPeminjaman] = daftar_item
        self._tanggal_peminjaman: date = tanggal_peminjaman
        self._batas_pengembalian: date = batas_pengembalian
        self._status: StatusTransaksi = StatusTransaksi.DIPINJAM

    @property
    def id_transaksi(self) -> str:
        return self._id_transaksi

    @property
    def mahasiswa(self) -> Mahasiswa:
        return self._mahasiswa

    @property
    def daftar_item(self) -> List[ItemPeminjaman]:
        return self._daftar_item

    @property
    def tanggal_peminjaman(self) -> date:
        return self._tanggal_peminjaman

    @property
    def batas_pengembalian(self) -> date:
        return self._batas_pengembalian

    @property
    def status(self) -> StatusTransaksi:
        return self._status

    def validasi_batas(self) -> bool:
        """Memeriksa apakah batas pengembalian tidak melebihi 7 hari dari tanggal pinjam."""
        selisih = self._batas_pengembalian - self._tanggal_peminjaman
        return timedelta(days=0) < selisih <= timedelta(days=self.MAKS_HARI)

    def kembalikan_alat(self, kode_alat: str, kondisi: KondisiAlat, tanggal: date) -> None:
        """Mengembalikan satu item alat tertentu dan memperbarui status transaksi secara keseluruhan."""
        for item in self._daftar_item:
            if item.alat.kode_alat == kode_alat and not item.sudah_kembali:
                item.tandai_kembali(kondisi, tanggal)
                self.hitung_status()
                return
        raise ValueError(f"Alat dengan kode '{kode_alat}' tidak ditemukan dalam transaksi ini atau sudah dikembalikan.")

    def hitung_status(self) -> StatusTransaksi:
        """Menghitung ulang status transaksi berdasarkan status item-itemnya."""
        jumlah_kembali = sum(1 for item in self._daftar_item if item.sudah_kembali)
        if jumlah_kembali == len(self._daftar_item):
            self._status = StatusTransaksi.SELESAI
            self._mahasiswa.hapus_transaksi_aktif(self)
        elif jumlah_kembali > 0:
            self._status = StatusTransaksi.SEBAGIAN_DIKEMBALIKAN
        else:
            self._status = StatusTransaksi.DIPINJAM
        return self._status

    def masih_aktif(self) -> bool:
        """True jika status bukan SELESAI."""
        return self._status != StatusTransaksi.SELESAI

    def alat_belum_kembali(self) -> List[ItemPeminjaman]:
        """Mengembalikan list item alat yang belum dikembalikan."""
        return [item for item in self._daftar_item if not item.sudah_kembali]

    def __repr__(self) -> str:
        return f"<Transaksi {self._id_transaksi}: {self._mahasiswa.nama} [{self._status.value}] ({len(self._daftar_item)} item)>"
