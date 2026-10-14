"""
Modul Fitur 8: Tampilkan Alat yang Sedang Dipinjam
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_tampilkan_alat_dipinjam(lab: 'LabManager') -> None:
    """
    Fungsi untuk menampilkan daftar alat yang berstatus DIPINJAM,
    lengkap dengan peminjam dan batas pengembalian.
    Parameter:
        lab (LabManager): Instance utama pengelola laboratorium
    """
    print("\n=== DAFTAR ALAT SEDANG DIPINJAM ===")
    daftar_alat = lab.tampilkan_alat_dipinjam()

    if not daftar_alat:
        print("Tidak ada alat yang sedang dipinjam.")
        return

    # Petakan kode alat -> transaksi yang masih memegang alat tersebut
    peminjam = {}
    for trx in lab.transaksi.values():
        for item in trx.alat_belum_kembali():
            peminjam[item.alat.kode_alat] = trx

    for nomor, alat in enumerate(daftar_alat, start=1):
        print(f"{nomor}. [{alat.kode_alat}] {alat.nama} | Kategori: {alat.kategori}")
        trx = peminjam.get(alat.kode_alat)
        if trx:
            print(f"   Peminjam      : {trx.mahasiswa.nama} ({trx.mahasiswa.nim})")
            print(f"   Transaksi     : {trx.id_transaksi}")
            print(f"   Batas kembali : {trx.batas_pengembalian}")
    print(f"\nTotal: {len(daftar_alat)} alat sedang dipinjam.")
