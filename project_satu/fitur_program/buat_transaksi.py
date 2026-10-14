# Buat Transaksi (Vicko)

from datetime import date, timedelta   
class ItemPeminjaman:
    def __init__(self, alat):
        self.alat = alat                  
        self.sudah_kembali = False        
        self.tanggal_kembali = None       
        self.kondisi_kembali = None       

    def tandai_kembali(self, kondisi, tanggal):
        self.sudah_kembali = True         
        self.tanggal_kembali = tanggal    
        self.kondisi_kembali = kondisi    

class Transaksi:
    def __init__(self, id_transaksi, mahasiswa, daftar_item, tanggal_peminjaman, batas_pengembalian):
        self.id_transaksi = id_transaksi
        self.mahasiswa = mahasiswa
        self.daftar_item = daftar_item                    
        self.tanggal_peminjaman = tanggal_peminjaman
        self.batas_pengembalian = batas_pengembalian
        self.status = "dipinjam"                         

    def alat_belum_kembali(self):
        hasil = []                                        
        for item in self.daftar_item:                     
            if not item.sudah_kembali:                    
                hasil.append(item)                        
        return hasil

    def hitung_status(self):
        jumlah_belum = len(self.alat_belum_kembali())     
        if jumlah_belum == len(self.daftar_item):         
            return "dipinjam"
        if jumlah_belum == 0:                            
            return "selesai"
        return "sebagian dikembalikan"                    

    def masih_aktif(self):
        return self.status != "selesai"                   

    def kembalikan_alat(self, kode_alat, kondisi, tanggal):
        for item in self.daftar_item:                     
            if item.alat.kode_alat == kode_alat and not item.sudah_kembali:
                item.tandai_kembali(kondisi, tanggal)     
                item.alat.terima_kembali(kondisi)         
                self.status = self.hitung_status()        
                return                                    
        raise ValueError("Alat tidak ada di transaksi ini atau sudah dikembalikan.")

def buat_transaksi(lab, nim, daftar_kode_alat, lama_hari):
    if nim not in lab.mahasiswa:
        raise ValueError("Mahasiswa tidak ditemukan.")
    mhs = lab.mahasiswa[nim]

    if not mhs.boleh_meminjam():                          
        raise ValueError("Mahasiswa sudah memiliki 2 transaksi aktif.")

    if len(daftar_kode_alat) == 0:
        raise ValueError("Pilih minimal satu alat.")

    if len(set(daftar_kode_alat)) != len(daftar_kode_alat):   
        raise ValueError("Ada alat yang dipilih lebih dari satu kali.")

    if lama_hari < 1 or lama_hari > 7:                   
        raise ValueError("Lama peminjaman harus 1 sampai 7 hari.")

    for kode in daftar_kode_alat:
        if kode not in lab.alat:
            raise ValueError("Alat " + kode + " tidak ditemukan.")
        if not lab.alat[kode].tersedia():               
            raise ValueError("Alat " + kode + " tidak tersedia.")

    daftar_item = []
    for kode in daftar_kode_alat:
        alat = lab.alat[kode]
        alat.tandai_dipinjam()                           
        daftar_item.append(ItemPeminjaman(alat))          

    id_baru = "T" + str(len(lab.transaksi) + 1).zfill(3)  
    hari_ini = date.today()
    batas = hari_ini + timedelta(days=lama_hari)          

    transaksi = Transaksi(id_baru, mhs, daftar_item, hari_ini, batas)
    lab.transaksi[id_baru] = transaksi                   
    mhs.tambah_transaksi_aktif(transaksi)                
    lab.catat_log("Transaksi " + id_baru + " dibuat oleh " + nim)
    return transaksi

def menu_buat_transaksi(lab):
    nim = input("NIM mahasiswa: ").strip()
    teks = input("Kode alat (pisahkan dengan koma): ")
    daftar_kode = [k.strip() for k in teks.split(",") if k.strip()]  
    try:
        lama = int(input("Lama peminjaman (1-7 hari): "))
        t = buat_transaksi(lab, nim, daftar_kode, lama)
        print("Berhasil! ID transaksi:", t.id_transaksi, "| Batas kembali:", t.batas_pengembalian)
    except ValueError as e:                               
        print("Gagal:", e)
