"""
Modul Fitur 1: Kelola Data Mahasiswa (Tambah, Edit, Hapus, Cari)
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_kelola_mahasiswa(lab: 'LabManager') -> None:
    """
    Sub-menu atau fungsi untuk mengelola data mahasiswa.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== KELOLA DATA MAHASISWA ===")
    # TODO: Anggota tim dapat mengimplementasikan alur input dan pemanggilan method lab di sini:
    # - lab.tambah_mahasiswa(nim, nama, nomor_hp)
    # - lab.edit_mahasiswa(nim, nama, nomor_hp)
    # - lab.hapus_mahasiswa(nim)
    # - lab.cari_mahasiswa(keyword)
    pass
