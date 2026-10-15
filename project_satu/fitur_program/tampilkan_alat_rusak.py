"""
Modul Fitur 9: Tampilkan Alat yang Rusak
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_tampilkan_alat_rusak(lab: 'LabManager') -> None:
    print("\n=== DAFTAR ALAT RUSAK ===")
    daftar_alat = lab.tampilkan_alat_rusak()

    if not daftar_alat:
        print("Tidak ada alat yang rusak.")
        return

    for nomor, alat in enumerate(daftar_alat, start=1):
        print(f"{nomor}. [{alat.kode_alat}] {alat.nama} | "
              f"Kategori: {alat.kategori} | Kondisi: {alat.kondisi.value}")
    print(f"\nTotal: {len(daftar_alat)} alat rusak.")
