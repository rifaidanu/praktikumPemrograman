from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .transaksi import Transaksi


class Mahasiswa:
    """Mewakili data mahasiswa dan melacak transaksi aktifnya."""
    MAKS_TRANSAKSI_AKTIF: int = 2

    def __init__(self, nim: str, nama: str, nomor_hp: str) -> None:
        self._nim: str = nim
        self._nama: str = nama
        self._nomor_hp: str = nomor_hp
        self._daftar_transaksi_aktif: List['Transaksi'] = []

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, value: str) -> None:
        self._nama = value

    @property
    def nomor_hp(self) -> str:
        return self._nomor_hp

    @nomor_hp.setter
    def nomor_hp(self, value: str) -> None:
        self._nomor_hp = value

    @property
    def daftar_transaksi_aktif(self) -> List['Transaksi']:
        return self._daftar_transaksi_aktif

    def boleh_meminjam(self) -> bool:
        """True jika jumlah transaksi aktif kurang dari batas maksimal (2)."""
        return len(self._daftar_transaksi_aktif) < self.MAKS_TRANSAKSI_AKTIF

    def tambah_transaksi_aktif(self, transaksi: 'Transaksi') -> None:
        """Menambahkan transaksi baru ke daftar transaksi aktif."""
        self._daftar_transaksi_aktif.append(transaksi)

    def hapus_transaksi_aktif(self, transaksi: 'Transaksi') -> None:
        """Menghapus transaksi dari daftar aktif setelah semua alat dikembalikan (selesai)."""
        if transaksi in self._daftar_transaksi_aktif:
            self._daftar_transaksi_aktif.remove(transaksi)

    def punya_peminjaman_aktif(self) -> bool:
        """True jika mahasiswa masih memiliki transaksi yang belum selesai."""
        return len(self._daftar_transaksi_aktif) > 0

    def __repr__(self) -> str:
        return f"<Mahasiswa {self._nim} - {self._nama} (Aktif: {len(self._daftar_transaksi_aktif)})>"
