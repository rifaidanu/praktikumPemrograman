import os
import sys
from collections import Counter
from typing import TYPE_CHECKING, Dict, List

if TYPE_CHECKING:
    from services.lab_manager import LabManager
    from models.transaksi import Transaksi


def hitung_statistik_peminjaman(lab: 'LabManager') -> dict:
    """Menghitung agregasi data statistik dari transaksi di laboratorium."""
    transaksi_list: List['Transaksi'] = list(lab.transaksi.values())

    # 1. Hitung transaksi selesai dan aktif
    transaksi_selesai = sum(1 for t in transaksi_list if not t.masih_aktif())
    transaksi_aktif = sum(1 for t in transaksi_list if t.masih_aktif())

    # Rincian status aktif
    transaksi_dipinjam = sum(1 for t in transaksi_list if t.status.value == "dipinjam")
    transaksi_sebagian = sum(1 for t in transaksi_list if t.status.value == "sebagian dikembalikan")

    # 2. Hitung frekuensi peminjaman alat
    frekuensi_alat: Counter = Counter()
    nama_alat_map: Dict[str, str] = {}
    for t in transaksi_list:
        for item in t.daftar_item:
            kode = item.alat.kode_alat
            frekuensi_alat[kode] += 1
            nama_alat_map[kode] = item.alat.nama

    # 3. Hitung frekuensi peminjaman per mahasiswa
    frekuensi_mhs: Counter = Counter()
    nama_mhs_map: Dict[str, str] = {}
    for t in transaksi_list:
        nim = t.mahasiswa.nim
        frekuensi_mhs[nim] += 1
        nama_mhs_map[nim] = t.mahasiswa.nama

    return {
        "total_transaksi": len(transaksi_list),
        "transaksi_selesai": transaksi_selesai,
        "transaksi_aktif": transaksi_aktif,
        "transaksi_dipinjam": transaksi_dipinjam,
        "transaksi_sebagian": transaksi_sebagian,
        "frekuensi_alat": frekuensi_alat,
        "nama_alat_map": nama_alat_map,
        "frekuensi_mhs": frekuensi_mhs,
        "nama_mhs_map": nama_mhs_map,
    }


def menu_statistik_peminjaman(lab: 'LabManager') -> None:
    """Menampilkan tampilan antarmuka statistik peminjaman laboratorium."""
    data = hitung_statistik_peminjaman(lab)

    print("\n" + "=" * 60)
    print("           STATISTIK PEMINJAMAN LABORATORIUM")
    print("=" * 60)

    # ---------------- 1. STATUS TRANSAKSI ----------------
    print("\n[ 1. RINGKASAN STATUS TRANSAKSI ]")
    print("-" * 60)
    print(f" • Jumlah Transaksi Selesai       : {data['transaksi_selesai']} transaksi")
    print(f" • Jumlah Transaksi Masih Aktif   : {data['transaksi_aktif']} transaksi")
    if data['transaksi_aktif'] > 0:
        print(f"    - Status Sedang Dipinjam      : {data['transaksi_dipinjam']}")
        print(f"    - Status Sebagian Kembali     : {data['transaksi_sebagian']}")
    print(f" • Total Seluruh Transaksi        : {data['total_transaksi']} transaksi")
    print("-" * 60)

    # ---------------- 2. ALAT PALING SERING DIPINJAM ----------------
    print("\n[ 2. ALAT YANG PALING SERING DIPINJAM ]")
    print("-" * 60)
    frekuensi_alat = data["frekuensi_alat"]
    nama_alat_map = data["nama_alat_map"]

    if not frekuensi_alat:
        print(" [INFO] Belum ada data peminjaman alat.")
    else:
        max_alat_count = max(frekuensi_alat.values())
        alat_terpopuler = [
            (kode, nama_alat_map[kode], count)
            for kode, count in frekuensi_alat.items()
            if count == max_alat_count
        ]

        print(f" Frekuensi Tertinggi : {max_alat_count} kali dipinjam")
        print(f"{'KODE':<10} {'NAMA ALAT':<32} {'DIPINJAM':<10}")
        print("-" * 55)
        for kode, nama, count in alat_terpopuler:
            print(f"{kode:<10} {nama:<32} {count:>3} kali")
        print("-" * 55)

        # Jika ada alat lain, tampilkan ranking lengkap
        if len(frekuensi_alat) > len(alat_terpopuler):
            print("\n  Daftar Peringkat Seluruh Alat yang Pernah Dipinjam:")
            for rank, (kode, count) in enumerate(frekuensi_alat.most_common(), 1):
                nama = nama_alat_map.get(kode, "-")
                print(f"  {rank:>2}. [{kode}] {nama:<30} : {count}x")

    # ---------------- 3. MAHASISWA PALING SERING MEMINJAM ----------------
    print("\n[ 3. MAHASISWA PALING SERING MELAKUKAN PEMINJAMAN ]")
    print("-" * 60)
    frekuensi_mhs = data["frekuensi_mhs"]
    nama_mhs_map = data["nama_mhs_map"]

    if not frekuensi_mhs:
        print(" [INFO] Belum ada transaksi oleh mahasiswa.")
    else:
        max_mhs_count = max(frekuensi_mhs.values())
        mhs_teraktif = [
            (nim, nama_mhs_map[nim], count)
            for nim, count in frekuensi_mhs.items()
            if count == max_mhs_count
        ]

        print(f" Frekuensi Tertinggi : {max_mhs_count} kali transaksi")
        print(f"{'NIM':<10} {'NAMA MAHASISWA':<32} {'TRANSAKSI':<12}")
        print("-" * 55)
        for nim, nama, count in mhs_teraktif:
            print(f"{nim:<10} {nama:<32} {count:>3} kali")
        print("-" * 55)

        # Jika ada mahasiswa lain, tampilkan ranking lengkap
        if len(frekuensi_mhs) > len(mhs_teraktif):
            print("\n  Daftar Peringkat Seluruh Mahasiswa yang Pernah Meminjam:")
            for rank, (nim, count) in enumerate(frekuensi_mhs.most_common(), 1):
                nama = nama_mhs_map.get(nim, "-")
                print(f"  {rank:>2}. [{nim}] {nama:<30} : {count}x transaksi")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    # Memungkinkan file dijalankan langsung secara mandiri untuk pengujian
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    from services.lab_manager import LabManager
    from data.dummy_data import inisialisasi_dummy_data

    lab = LabManager()
    inisialisasi_dummy_data(lab)

    print("\n>>> Menjalankan Modul Statistik Peminjaman secara Mandiri (Standalone)...")
    menu_statistik_peminjaman(lab)
