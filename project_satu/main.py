"""
Program Utama Sistem Peminjaman Alat Laboratorium
"""
from services.lab_manager import LabManager
from fitur_program.menu_utama import tampilkan_menu_utama


def main() -> None:
    # Inisialisasi pengelola pusat data & logika bisnis laboratorium
    lab = LabManager()

    # (Opsional) Anggota tim dapat menambahkan seeder/dummy data awal di sini jika diperlukan
    # Contoh:
    # lab.tambah_mahasiswa("M001", "Andi", "08123456789")
    # lab.tambah_alat("ALT-001", "Multimeter Digital", "Elektronika")

    # Jalankan menu utama interaktif
    tampilkan_menu_utama(lab)


if __name__ == "__main__":
    main()
