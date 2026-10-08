"""
Modul Fitur 7: Tampilkan Alat yang Tersedia
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_tampilkan_alat_tersedia(lab: 'LabManager') -> None:
    """
    Fungsi untuk menampilkan daftar semua peralatan yang berstatus TERSEDIA.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== DAFTAR ALAT TERSEDIA ===")
    # TODO: Anggota tim dapat mengimplementasikan tampilan alat tersedia di sini:
    # - lab.tampilkan_alat_tersedia()
    pass
