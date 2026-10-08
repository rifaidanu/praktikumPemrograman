"""
Modul Fitur 4: Tampilkan Transaksi
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_tampilkan_transaksi(lab: 'LabManager') -> None:
    """
    Fungsi untuk menampilkan seluruh transaksi peminjaman.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== DAFTAR TRANSAKSI PEMINJAMAN ===")
    # TODO: Anggota tim dapat mengimplementasikan tampilan daftar transaksi di sini:
    # - lab.tampilkan_transaksi()
    pass
