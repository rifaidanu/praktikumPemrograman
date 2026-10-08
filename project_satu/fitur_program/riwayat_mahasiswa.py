"""
Modul Fitur 10: Tampilkan Riwayat Peminjaman Mahasiswa
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_riwayat_mahasiswa(lab: 'LabManager') -> None:
    """
    Fungsi untuk menampilkan seluruh riwayat peminjaman mahasiswa (aktif maupun selesai).
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== RIWAYAT PEMINJAMAN MAHASISWA ===")
    # TODO: Anggota tim dapat mengimplementasikan alur tampilan riwayat mahasiswa di sini:
    # - lab.riwayat_mahasiswa(nim)
    pass
