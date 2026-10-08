"""
Modul Menu Utama: Penghubung (Router) antar fitur program
"""
from services.lab_manager import LabManager

from .kelola_mahasiswa import menu_kelola_mahasiswa
from .kelola_alat import menu_kelola_alat
from .buat_transaksi import menu_buat_transaksi
from .tampilkan_transaksi import menu_tampilkan_transaksi
from .proses_pengembalian import menu_proses_pengembalian
from .cari_transaksi import menu_cari_transaksi
from .tampilkan_alat_tersedia import menu_tampilkan_alat_tersedia
from .tampilkan_alat_dipinjam import menu_tampilkan_alat_dipinjam
from .tampilkan_alat_rusak import menu_tampilkan_alat_rusak
from .riwayat_mahasiswa import menu_riwayat_mahasiswa


def tampilkan_menu_utama(lab: LabManager) -> None:
    """Loop utama untuk menampilkan menu aplikasi laboratorium."""
    while True:
        print("\n" + "=" * 55)
        print("    SISTEM INFORMASI PEMINJAMAN ALAT LABORATORIUM")
        print("=" * 55)
        print(" 1. Kelola Data Mahasiswa (Tambah, Edit, Hapus, Cari)")
        print(" 2. Kelola Data Alat (Tambah, Edit, Hapus, Cari)")
        print(" 3. Buat Transaksi Peminjaman")
        print(" 4. Tampilkan Semua Transaksi")
        print(" 5. Proses Pengembalian Alat")
        print(" 6. Cari Transaksi Berdasarkan Mahasiswa")
        print(" 7. Tampilkan Alat yang Tersedia")
        print(" 8. Tampilkan Alat yang Sedang Dipinjam")
        print(" 9. Tampilkan Alat yang Rusak")
        print("10. Tampilkan Riwayat Peminjaman Mahasiswa")
        print(" 0. Keluar dari Program")
        print("=" * 55)

        pilihan = input("Pilih menu [0-10]: ").strip()

        if pilihan == "1":
            menu_kelola_mahasiswa(lab)
        elif pilihan == "2":
            menu_kelola_alat(lab)
        elif pilihan == "3":
            menu_buat_transaksi(lab)
        elif pilihan == "4":
            menu_tampilkan_transaksi(lab)
        elif pilihan == "5":
            menu_proses_pengembalian(lab)
        elif pilihan == "6":
            menu_cari_transaksi(lab)
        elif pilihan == "7":
            menu_tampilkan_alat_tersedia(lab)
        elif pilihan == "8":
            menu_tampilkan_alat_dipinjam(lab)
        elif pilihan == "9":
            menu_tampilkan_alat_rusak(lab)
        elif pilihan == "10":
            menu_riwayat_mahasiswa(lab)
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan sistem peminjaman laboratorium!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan masukkan angka antara 0 - 10.")
