"""
Modul Fitur 3: Buat Transaksi Peminjaman
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_buat_transaksi(lab: 'LabManager') -> None:
    """
    Fungsi untuk alur pembuatan transaksi peminjaman alat.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== BUAT TRANSAKSI PEMINJAMAN ===")
    # TODO: Anggota tim dapat mengimplementasikan alur input dan pemanggilan method lab di sini:
    # - lab.buat_transaksi(nim, daftar_kode_alat, batas)
    pass
