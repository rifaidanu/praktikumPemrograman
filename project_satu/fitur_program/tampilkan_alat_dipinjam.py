"""
Modul Fitur 8: Tampilkan Alat yang Sedang Dipinjam
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_tampilkan_alat_dipinjam(lab: 'LabManager') -> None:
    """
    Fungsi untuk menampilkan daftar semua peralatan yang berstatus DIPINJAM.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== DAFTAR ALAT SEDANG DIPINJAM ===")
    # TODO: Anggota tim dapat mengimplementasikan tampilan alat yang sedang dipinjam di sini:
    # - lab.tampilkan_alat_dipinjam()
    pass
