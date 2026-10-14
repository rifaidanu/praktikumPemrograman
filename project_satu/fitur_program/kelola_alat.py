# =========================================================
# FITUR 2: KELOLA DATA ALAT LABORATORIUM (Tugas Tama)
# =========================================================
from models.enums import KondisiAlat

def kelola_alat(lab):
    """
    Submenu interaktif untuk pengelolaan data alat laboratorium (CRUD).
    Menerima parameter `lab` yang merupakan instance dari LabManager.
    """
    while True:
        print("\n" + "=" * 50)
        print("          SUBMENU KELOLA DATA ALAT LAB        ")
        print("=" * 50)
        print("1. Tambah Alat Lab Baru")
        print("2. Edit Data Alat Lab")
        print("3. Hapus Data Alat Lab")
        print("4. Cari Alat Lab")
        print("5. Tampilkan Seluruh Alat Lab")
        print("0. Kembali ke Menu Utama")
        print("=" * 50)
        
        pilihan = input("Pilih menu (0-5): ").strip()
        
        # --------------------------------------------------
        # 1. TAMBAH ALAT
        # --------------------------------------------------
        if pilihan == "1":
            print("\n--- TAMBAH ALAT LAB BARU ---")
            kode_alat = input("Masukkan Kode Alat (misal ALT-001): ").strip().upper()
            nama = input("Masukkan Nama Alat               : ").strip().title()
            kategori = input("Masukkan Kategori Alat           : ").strip().title()
            
            print("\nPilih Kondisi Awal Alat:")
            print("1. Baik")
            print("2. Rusak Ringan")
            print("3. Rusak Berat")
            p_kondisi = input("Pilih kondisi (1-3, default=1)  : ").strip()
            
            kondisi = KondisiAlat.BAIK
            if p_kondisi == "2":
                kondisi = KondisiAlat.RUSAK_RINGAN
            elif p_kondisi == "3":
                kondisi = KondisiAlat.RUSAK_BERAT
                
            try:
                lab.tambah_alat(kode_alat, nama, kategori, kondisi)
                print(f"[SUCCESS] Alat '{nama}' ({kode_alat}) berhasil ditambahkan!")
            except ValueError as e:
                print(f"[ERROR] {e}")

        # --------------------------------------------------
        # 2. EDIT ALAT
        # --------------------------------------------------
        elif pilihan == "2":
            print("\n--- EDIT DATA ALAT LAB ---")
            kode_alat = input("Masukkan Kode Alat yang ingin diedit: ").strip().upper()
            
            if kode_alat not in lab.alat:
                print(f"[ERROR] Alat dengan kode '{kode_alat}' tidak ditemukan.")
                continue
            
            alat_lama = lab.alat[kode_alat]
            print(f"Data Saat Ini -> Nama: {alat_lama.nama}, Kategori: {alat_lama.kategori}, Kondisi: {alat_lama.kondisi.value}")
            
            nama_baru = input("Nama Baru (Enter jika tidak diubah)     : ").strip().title()
            kat_baru = input("Kategori Baru (Enter jika tidak diubah) : ").strip().title()
            
            print("\nUbah Kondisi Alat? (1: Baik, 2: Rusak Ringan, 3: Rusak Berat, Enter jika tidak diubah)")
            p_kondisi = input("Pilihan kondisi: ").strip()
            
            nama_final = nama_baru if nama_baru else alat_lama.nama
            kat_final = kat_baru if kat_baru else alat_lama.kategori
            
            kondisi_final = alat_lama.kondisi
            if p_kondisi == "1":
                kondisi_final = KondisiAlat.BAIK
            elif p_kondisi == "2":
                kondisi_final = KondisiAlat.RUSAK_RINGAN
            elif p_kondisi == "3":
                kondisi_final = KondisiAlat.RUSAK_BERAT

            try:
                lab.edit_alat(kode_alat, nama_final, kat_final, kondisi_final)
                print(f"[SUCCESS] Data alat '{kode_alat}' berhasil diperbarui!")
            except ValueError as e:
                print(f"[ERROR] {e}")

        # --------------------------------------------------
        # 3. HAPUS ALAT
        # --------------------------------------------------
        elif pilihan == "3":
            print("\n--- HAPUS DATA ALAT LAB ---")
            kode_alat = input("Masukkan Kode Alat yang akan dihapus: ").strip().upper()
            
            try:
                lab.hapus_alat(kode_alat)
                print(f"[SUCCESS] Alat dengan kode '{kode_alat}' berhasil dihapus.")
            except ValueError as e:
                print(f"[ERROR] {e}")

        # --------------------------------------------------
        # 4. CARI ALAT
        # --------------------------------------------------
        elif pilihan == "4":
            print("\n--- CARI ALAT LAB ---")
            keyword = input("Masukkan Keyword (Kode / Nama / Kategori): ").strip()
            
            hasil = lab.cari_alat(keyword)
            if hasil:
                print("\n" + "-" * 65)
                print(f"{'KODE':<10} {'NAMA ALAT':<22} {'KATEGORI':<18} {'KONDISI':<12}")
                print("-" * 65)
                for alt in hasil:
                    print(f"{alt.kode_alat:<10} {alt.nama:<22} {alt.kategori:<18} {alt.kondisi.value:<12}")
                print("-" * 65)
            else:
                print(f"[INFO] Tidak ada alat yang cocok dengan '{keyword}'.")

        # --------------------------------------------------
        # 5. TAMPILKAN SELURUH ALAT
        # --------------------------------------------------
        elif pilihan == "5":
            print("\n--- DAFTAR SELURUH ALAT LAB ---")
            daftar_alat = list(lab.alat.values())
            
            if daftar_alat:
                print("\n" + "-" * 75)
                print(f"{'KODE':<10} {'NAMA ALAT':<22} {'KATEGORI':<18} {'KONDISI':<13} {'STATUS':<12}")
                print("-" * 75)
                for alt in daftar_alat:
                    print(f"{alt.kode_alat:<10} {alt.nama:<22} {alt.kategori:<18} {alt.kondisi.value:<13} {alt.status.value:<12}")
                print("-" * 75)
                print(f"Total Alat: {len(daftar_alat)} unit")
            else:
                print("[INFO] Belum ada data alat terdaftar.")

        # --------------------------------------------------
        # 0. KEMBALI
        # --------------------------------------------------
        elif pilihan == "0":
            break
        else:
            print("[ERROR] Pilihan menu tidak valid. Pilih angka 0-5.")
