"""
Modul Fitur 9: Tampilkan Alat yang Rusak
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_tampilkan_alat_rusak(lab: 'LabManager') -> None:
    """
    Fungsi untuk menampilkan daftar semua peralatan yang berkondisi rusak (rusak ringan / berat).
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== DAFTAR ALAT RUSAK ===")
    # TODO: Anggota tim dapat mengimplementasikan tampilan alat rusak di sini:
    # - lab.tampilkan_alat_rusak()
    pass
