"""
Modul Fitur 7: Tampilkan Alat yang Tersedia
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_tampilkan_alat_tersedia(lab: 'LabManager') -> None:
    alat_tersedia = lab.tampilkan_alat_tersedia()

    for i in alat_tersedia:
        print(i)
