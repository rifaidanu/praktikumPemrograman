
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def menu_riwayat_mahasiswa(lab: 'LabManager') -> None:
    print("\n=== RIWAYAT PEMINJAMAN MAHASISWA ===")
    nim = input("Masukkan NIM mahasiswa: ").strip()

    try:
        riwayat = lab.riwayat_mahasiswa(nim)
    except ValueError as e:
        print(f"[GAGAL] {e}")
        return

    mhs = lab.mahasiswa[nim]
    print(f"Riwayat peminjaman: {mhs.nama} ({mhs.nim})")

    if not riwayat:
        print("Belum ada riwayat peminjaman.")
        return

    for trx in riwayat:
        print(f"\n[{trx.id_transaksi}] Pinjam {trx.tanggal_peminjaman} | "
              f"Batas {trx.batas_pengembalian} | Status: {trx.status.value}")
        for item in trx.daftar_item:
            if item.sudah_kembali:
                ket = (f"dikembalikan {item.tanggal_kembali}, "
                       f"kondisi {item.kondisi_kembali.value}")
            else:
                ket = "masih dipinjam"
            print(f"   - {item.alat.kode_alat} {item.alat.nama}: {ket}")
    print(f"\nTotal: {len(riwayat)} transaksi.")
