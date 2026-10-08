"""
Modul Fitur 6: Cari Transaksi Berdasarkan Mahasiswa
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_cari_transaksi(lab: 'LabManager') -> None:
    """
    Fungsi untuk mencari transaksi peminjaman milik mahasiswa berdasarkan NIM.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== CARI TRANSAKSI BERDASARKAN MAHASISWA ===")
    # TODO: Anggota tim dapat mengimplementasikan alur pencarian transaksi mahasiswa di sini:
    # - lab.cari_transaksi_by_mahasiswa(nim)
    pass
