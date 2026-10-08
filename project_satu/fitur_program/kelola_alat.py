"""
Modul Fitur 2: Kelola Data Alat (Tambah, Edit, Hapus, Cari)
"""
from typing import TYPE_CHECKING
from models.enums import KondisiAlat

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_kelola_alat(lab: 'LabManager') -> None:
    """
    Sub-menu atau fungsi untuk mengelola data peralatan lab.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== KELOLA DATA ALAT ===")
    # TODO: Anggota tim dapat mengimplementasikan alur input dan pemanggilan method lab di sini:
    # - lab.tambah_alat(kode_alat, nama, kategori, kondisi)
    # - lab.edit_alat(kode_alat, nama, kategori, kondisi)
    # - lab.hapus_alat(kode_alat)
    # - lab.cari_alat(keyword)
    pass
