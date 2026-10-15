"""
Modul Fitur 6: Cari Transaksi Berdasarkan Mahasiswa
"""
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from services.lab_manager import LabManager
    from models.transaksi import Transaksi


def cari_transaksi_by_mahasiswa(lab: 'LabManager', nim: str) -> None:
    """
    Mencari dan menampilkan seluruh transaksi milik mahasiswa berdasarkan NIM.

    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
        nim (str): Nomor Induk Mahasiswa
    """
    # Toleransi pencarian NIM huruf kapital
    target_nim = nim
    if target_nim not in lab.mahasiswa and target_nim.upper() in lab.mahasiswa:
        target_nim = target_nim.upper()

    # 2. Cek apakah mahasiswa terdaftar di sistem
    if target_nim not in lab.mahasiswa:
        print(f"\n[ERROR] Mahasiswa dengan NIM '{nim}' tidak ditemukan di sistem.")
        return

    mhs = lab.mahasiswa[target_nim]

    # 4. Tampilkan informasi mahasiswa (Nama, NIM, jumlah transaksi yang sedang aktif)
    print("\n" + "=" * 60)
    print("             INFORMASI MAHASISWA")
    print("=" * 60)
    print(f" NIM             : {mhs.nim}")
    print(f" Nama Mahasiswa  : {mhs.nama}")
    print(f" Nomor HP        : {mhs.nomor_hp}")
    print(f" Transaksi Aktif : {len(mhs.daftar_transaksi_aktif)} transaksi")
    print("=" * 60)

    # 3. Panggil lab.cari_transaksi_by_mahasiswa(nim)
    daftar_transaksi: List['Transaksi'] = lab.cari_transaksi_by_mahasiswa(target_nim)

    # 5. Jika tidak ada transaksi, tampilkan pesan bahwa mahasiswa belum pernah meminjam
    if not daftar_transaksi:
        print(f"\n[INFO] Mahasiswa '{mhs.nama}' ({mhs.nim}) belum pernah melakukan transaksi peminjaman.\n")
        return

    # 6. Jika ada, lakukan perulangan dan cetak rincian ID transaksi, status, tanggal, serta status item alat-alatnya
    print(f"\nDitemukan {len(daftar_transaksi)} transaksi peminjaman:")
    for no, trx in enumerate(daftar_transaksi, start=1):
        status_str = (
            trx.status.value.upper()
            if hasattr(trx.status, 'value')
            else str(trx.status).upper()
        )
        print("\n" + "-" * 60)
        print(f" [{no}] ID Transaksi       : {trx.id_transaksi}")
        print(f"     Tanggal Pinjam     : {trx.tanggal_peminjaman}")
        print(f"     Batas Pengembalian : {trx.batas_pengembalian}")
        print(f"     Status Transaksi   : {status_str}")
        print("     Daftar Alat Dipinjam:")

        for item in trx.daftar_item:
            if item.sudah_kembali:
                kondisi = (
                    item.kondisi_kembali.value
                    if hasattr(item.kondisi_kembali, 'value')
                    else str(item.kondisi_kembali)
                )
                ket = f"Sudah kembali ({item.tanggal_kembali}, Kondisi: {kondisi})"
            else:
                ket = "Belum kembali (Masih dipinjam)"

            print(f"       • [{item.alat.kode_alat}] {item.alat.nama} ({item.alat.kategori})")
            print(f"         Status: {ket}")

    print("-" * 60)
    print(f"Total: {len(daftar_transaksi)} transaksi terdaftar untuk mahasiswa ini.\n")


def menu_cari_transaksi(lab: 'LabManager') -> None:
    """
    Submenu/form interaktif untuk fitur pencarian transaksi per mahasiswa.
    Dipanggil dari menu_utama.py pada pilihan menu nomor 6.
    """
    print("\n" + "=" * 60)
    print("         CARI TRANSAKSI BERDASARKAN MAHASISWA")
    print("=" * 60)

    # 1. Minta input NIM mahasiswa
    nim = input("Masukkan NIM mahasiswa: ").strip()

    if not nim:
        print("[ERROR] NIM tidak boleh kosong.")
        return

    cari_transaksi_by_mahasiswa(lab, nim)


# Alias untuk fleksibilitas pemanggilan
cari_transaksi = menu_cari_transaksi