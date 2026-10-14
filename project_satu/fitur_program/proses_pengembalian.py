from datetime import date                  

DAFTAR_KONDISI = ["baik", "rusak ringan", "rusak berat"]  

def proses_pengembalian(lab, id_transaksi, kode_alat, kondisi):
    if kondisi not in DAFTAR_KONDISI:                    
        raise ValueError("Kondisi harus: baik, rusak ringan, atau rusak berat.")
    if id_transaksi not in lab.transaksi:
        raise ValueError("Transaksi tidak ditemukan.")
    t = lab.transaksi[id_transaksi]
    if not t.masih_aktif():                              
        raise ValueError("Transaksi ini sudah selesai.")

    t.kembalikan_alat(kode_alat, kondisi, date.today())  
    lab.catat_log("Alat " + kode_alat + " dikembalikan (" + kondisi + ") pada " + id_transaksi)
    if not t.masih_aktif():                               
        t.mahasiswa.hapus_transaksi_aktif(t)            
        lab.catat_log("Transaksi " + id_transaksi + " selesai")
        
def menu_pengembalian(lab):
    id_t = input("ID transaksi: ").strip().upper()
    kode = input("Kode alat yang dikembalikan: ").strip()
    print("Kondisi: 1. Baik  2. Rusak ringan  3. Rusak berat")
    pilihan = input("Pilih (1/2/3): ").strip()
    daftar_pilihan = {                                
        "1": "baik",
        "2": "rusak ringan",
        "3": "rusak berat",
    }
    if pilihan not in daftar_pilihan:
        print("Gagal: pilihan kondisi tidak valid.")
        return
    try:
        proses_pengembalian(lab, id_t, kode, daftar_pilihan[pilihan])
        print("Pengembalian berhasil dicatat.")
    except ValueError as e:
        print("Gagal:", e)
