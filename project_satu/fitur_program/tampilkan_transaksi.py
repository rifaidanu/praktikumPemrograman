def tampilkan_transaksi(lab):
    if len(lab.transaksi) == 0:                         
        print("Belum ada transaksi.")
        return

    for t in lab.transaksi.values():                     
        print("=" * 40)
        print("ID Transaksi :", t.id_transaksi)
        print("Mahasiswa    :", t.mahasiswa.nim, "-", t.mahasiswa.nama)
        print("Tgl Pinjam   :", t.tanggal_peminjaman)
        print("Batas Kembali:", t.batas_pengembalian)
        print("Status       :", t.status.value if hasattr(t.status, 'value') else t.status)
        print("Daftar Alat  :")
        for item in t.daftar_item:                       
            if item.sudah_kembali:
                kondisi_str = item.kondisi_kembali.value if hasattr(item.kondisi_kembali, 'value') else str(item.kondisi_kembali)
                ket = f"kembali {item.tanggal_kembali} ({kondisi_str})"
            else:
                ket = "belum kembali"
            print("  -", item.alat.kode_alat, item.alat.nama, "|", ket)

def menu_tampilkan_transaksi(lab):
    tampilkan_transaksi(lab)

