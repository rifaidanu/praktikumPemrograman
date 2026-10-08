"""
Program Utama Sistem Peminjaman Alat Laboratorium
"""
from services.lab_manager import LabManager
from data.dummy_data import inisialisasi_dummy_data
from fitur_program.menu_utama import tampilkan_menu_utama


def main() -> None:
    # Inisialisasi pengelola pusat data & logika bisnis laboratorium
    lab = LabManager()

    # Memuat data awal/dummy (10 alat, mahasiswa, dan contoh transaksi awal)
    inisialisasi_dummy_data(lab)

    # Jalankan menu utama interaktif
    tampilkan_menu_utama(lab)


if __name__ == "__main__":
    main()
