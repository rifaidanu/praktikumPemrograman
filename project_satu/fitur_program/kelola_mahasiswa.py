def kelola_mahasiswa(lab):
    """
    Submenu interaktif untuk pengelolaan data mahasiswa (CRUD).
    Menerima parameter `lab` yang merupakan instance dari LabManager.
    """
    while True:
        print("\n" + "=" * 45)
        print("         SUBMENU KELOLA DATA MAHASISWA       ")
        print("=" * 45)
        print("1. Tambah Mahasiswa Baru")
        print("2. Edit Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Seluruh Mahasiswa")
        print("0. Kembali ke Menu Utama")
        print("=" * 45)
        
        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            print("\n--- TAMBAH MAHASISWA BARU ---")
            nim = input("Masukkan NIM      : ").strip().upper()
            nama = input("Masukkan Nama     : ").strip().title()
            nomor_hp = input("Masukkan No. HP   : ").strip()
            
            try:
                lab.tambah_mahasiswa(nim, nama, nomor_hp)
                print(f"[SUCCESS] Mahasiswa {nama} ({nim}) berhasil ditambahkan!")
            except ValueError as e:
                print(f"[ERROR] {e}")

        elif pilihan == "2":
            print("\n--- EDIT DATA MAHASISWA ---")
            nim = input("Masukkan NIM Mahasiswa yang ingin diedit: ").strip().upper()
            
            if nim not in lab.mahasiswa:
                print(f"[ERROR] Mahasiswa dengan NIM {nim} tidak ditemukan.")
                continue
            
            mhs_lama = lab.mahasiswa[nim]
            print(f"Data Saat Ini -> Nama: {mhs_lama.nama}, No HP: {mhs_lama.nomor_hp}")
            
            nama_baru = input("Nama Baru (tekan Enter jika tidak diubah) : ").strip().title()
            hp_baru = input("No HP Baru (tekan Enter jika tidak diubah): ").strip()
            
            nama_final = nama_baru if nama_baru else mhs_lama.nama
            hp_final = hp_baru if hp_baru else mhs_lama.nomor_hp
            
            try:
                lab.edit_mahasiswa(nim, nama_final, hp_final)
                print(f"[SUCCESS] Data mahasiswa {nim} berhasil diperbarui!")
            except ValueError as e:
                print(f"[ERROR] {e}")

        elif pilihan == "3":
            print("\n--- HAPUS DATA MAHASISWA ---")
            nim = input("Masukkan NIM Mahasiswa yang akan dihapus: ").strip().upper()
            
            try:
                lab.hapus_mahasiswa(nim)
                print(f"[SUCCESS] Mahasiswa dengan NIM {nim} berhasil dihapus.")
            except ValueError as e:
                print(f"[ERROR] {e}")

        elif pilihan == "4":
            print("\n--- CARI MAHASISWA ---")
            keyword = input("Masukkan Keyword (NIM / Nama): ").strip()
            
            hasil = lab.cari_mahasiswa(keyword)
            if hasil:
                print("\n" + "-" * 55)
                print(f"{'NIM':<12} {'NAMA MAHASISWA':<25} {'NO HP':<15}")
                print("-" * 55)
                for mhs in hasil:
                    print(f"{mhs.nim:<12} {mhs.nama:<25} {mhs.nomor_hp:<15}")
                print("-" * 55)
            else:
                print(f"[INFO] Tidak ada data mahasiswa yang cocok dengan '{keyword}'.")


        elif pilihan == "5":
            print("\n--- DAFTAR SELURUH MAHASISWA ---")
            daftar_mhs = list(lab.mahasiswa.values())
            
            if daftar_mhs:
                print("\n" + "-" * 55)
                print(f"{'NIM':<12} {'NAMA MAHASISWA':<25} {'NO HP':<15}")
                print("-" * 55)
                for mhs in daftar_mhs:
                    print(f"{mhs.nim:<12} {mhs.nama:<25} {mhs.nomor_hp:<15}")
                print("-" * 55)
                print(f"Total Mahasiswa: {len(daftar_mhs)} orang")
            else:
                print("[INFO] Belum ada data mahasiswa terdaftar.")

        elif pilihan == "0":
            break
        else:
            print("[ERROR] Pilihan menu tidak valid. Pilih angka 0-5.")
