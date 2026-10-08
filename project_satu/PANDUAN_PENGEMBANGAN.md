# Panduan Struktur Program dan Petunjuk Pengerjaan Fitur

Dokumen ini ditujukan untuk seluruh anggota tim pengembang sistem **Peminjaman Peralatan Laboratorium**. Dokumen ini menjelaskan struktur arsitektur modular yang telah disiapkan serta panduan langkah demi langkah bagi setiap anggota tim saat mengimplementasikan fiturnya masing-masing.

---

## 1. Arsitektur dan Struktur File Proyek

Proyek ini menggunakan pola arsitektur **Three-Tier Architecture** sederhana:
1. **Presentation Layer (`fitur_program/`)**: Bertanggung jawab menerima input dari terminal (`input()`), menampilkan teks/tabel, dan menangani error ke pengguna.
2. **Business Logic & Service Layer (`services/`)**: Pengatur alur, validasi aturan bisnis, dan penyimpanan state koleksi data (`LabManager`).
3. **Domain & Entity Layer (`models/`)**: Representasi objek nyata (`Mahasiswa`, `Peralatan`, `Transaksi`, `ItemPeminjaman`, dan Enum status).

```text
project_satu/
│
├── models/                           # 📦 Model data dan Enum
│   ├── __init__.py                   # Mempermudah import class model
│   ├── enums.py                      # StatusTransaksi, KondisiAlat, StatusAlat
│   ├── mahasiswa.py                  # Class Mahasiswa
│   ├── peralatan.py                  # Class Peralatan
│   └── transaksi.py                  # Class ItemPeminjaman & Transaksi
│
├── services/                         # ⚙️ Pengelola pusat logika & state data
│   ├── __init__.py                   # Export class LabManager
│   └── lab_manager.py                # Class LabManager (CRUD, validasi, orkestrator)
│
├── fitur_program/                    # 🖥️ Modul CLI Fitur (Tugas Anggota Tim)
│   ├── __init__.py
│   ├── kelola_mahasiswa.py           # [Fitur 1] Submenu CRUD Mahasiswa
│   ├── kelola_alat.py                # [Fitur 2] Submenu CRUD Alat Lab
│   ├── buat_transaksi.py             # [Fitur 3] Form Peminjaman Alat
│   ├── tampilkan_transaksi.py        # [Fitur 4] Tampilan Rincian Transaksi
│   ├── proses_pengembalian.py        # [Fitur 5] Form Pengembalian Alat
│   ├── cari_transaksi.py             # [Fitur 6] Pencarian Transaksi per Mahasiswa
│   ├── tampilkan_alat_tersedia.py    # [Fitur 7] Filter Alat Berstatus TERSEDIA
│   ├── tampilkan_alat_dipinjam.py    # [Fitur 8] Filter Alat Berstatus DIPINJAM
│   ├── tampilkan_alat_rusak.py       # [Fitur 9] Filter Alat Kondisi Rusak
│   ├── riwayat_mahasiswa.py          # [Fitur 10] Riwayat Lengkap Peminjaman Mahasiswa
│   └── menu_utama.py                 # Router pemanggil menu 1-10 & loop utama
│
├── PANDUAN_PENGEMBANGAN.md           # 📖 Dokumen ini
└── main.py                           # 🚀 Titik masuk eksekusi program
```

---

## 2. Prinsip Kerja Bersama (Team Conventions)

Agar tidak terjadi konflik (*merge conflict*) atau *bug*, setiap anggota tim wajib mematuhi aturan berikut:

1. **Bekerja Hanya di File Fitur Masing-Masing:**
   - Kerjakan alur hanya di dalam file yang ditugaskan di folder `fitur_program/`.
   - Hindari mengubah struktur class di `models/` atau `services/lab_manager.py` tanpa kesepakatan bersama.
2. **Jangan Mengakses / Mengubah Data Secara Langsung:**
   - Gunakan method resmi yang ada pada objek `lab` (misal: `lab.tambah_mahasiswa(...)`, bukan `lab._mahasiswa[nim] = ...`).
3. **Selalu Gunakan `try - except ValueError`:**
   - Semua validasi aturan bisnis di `LabManager` akan melempar `ValueError` jika ada syarat yang dilanggar. Tangkap error tersebut di file fitur dan tampilkan pesan kesalahan yang ramah kepada pengguna.
4. **Parameter `lab` Adalah Objek Utama:**
   - Setiap fungsi fitur menerima satu parameter bernama `lab` yang merupakan instance dari `LabManager`.

---

## 3. Langkah-Langkah Pengerjaan untuk Setiap Fitur

Berikut panduan alur logika (apa saja yang perlu disiapkan dan alur langkahnya) untuk masing-masing anggota tim:

---

### 🔹 Fitur 1: Kelola Data Mahasiswa (`fitur_program/kelola_mahasiswa.py`)
* **Tujuan:** Menyediakan sub-menu untuk menambah, mengedit, menghapus, mencari, dan melihat daftar mahasiswa.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Buat loop sub-menu pilihan (1. Tambah, 2. Edit, 3. Hapus, 4. Cari, 5. Tampil Semua, 0. Kembali).
  2. **Tambah:** Minta input NIM, Nama, Nomor HP. Panggil `lab.tambah_mahasiswa(nim, nama, nomor_hp)` dalam blok `try-except`.
  3. **Edit:** Minta input NIM yang akan diedit. Cek apakah ada di `lab.mahasiswa`. Jika ada, minta input nama baru / no HP baru (opsional), lalu panggil `lab.edit_mahasiswa(...)`.
  4. **Hapus:** Minta input NIM, panggil `lab.hapus_mahasiswa(nim)`. Tangkap error jika mahasiswa masih punya peminjaman aktif.
  5. **Cari:** Minta input keyword (NIM atau Nama), panggil `lab.cari_mahasiswa(keyword)`, lalu tampilkan hasilnya dalam format tabel.

---

### 🔹 Fitur 2: Kelola Data Alat (`fitur_program/kelola_alat.py`)
* **Tujuan:** Menyediakan sub-menu untuk mengelola unit fisik alat laboratorium.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Buat loop sub-menu pilihan (Tambah, Edit, Hapus, Cari, Tampil Semua).
  2. **Tambah:** Minta input Kode Alat (misal `ALT-001`), Nama Alat, Kategori, dan pilih Kondisi awal (`KondisiAlat.BAIK` / `RUSAK_RINGAN` / `RUSAK_BERAT`). Panggil `lab.tambah_alat(...)`.
  3. **Edit:** Minta Kode Alat, tampilkan data lama, minta input perubahan nama/kategori/kondisi baru, panggil `lab.edit_alat(...)`.
  4. **Hapus:** Minta Kode Alat, panggil `lab.hapus_alat(kode)`. Tangkap error jika alat masih tercatat di transaksi aktif.
  5. **Cari:** Minta keyword pencarian (kode/nama/kategori), panggil `lab.cari_alat(keyword)`, dan cetak hasilnya dalam format kolom/tabel.

---

### 🔹 Fitur 3: Buat Transaksi Peminjaman (`fitur_program/buat_transaksi.py`)
* **Tujuan:** Membuat transaksi baru untuk peminjaman satu atau beberapa alat sekaligus.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Tampilkan daftar alat yang saat ini `TERSEDIA` menggunakan `lab.tampilkan_alat_tersedia()` sebagai referensi peminjam.
  2. Minta input `NIM` mahasiswa peminjam.
  3. Minta input daftar `kode_alat` (bisa menerima beberapa kode yang dipisahkan koma atau input berulang).
  4. Minta input durasi peminjaman (dalam hari, maksimal 7 hari), lalu hitung tanggal batas pengembalian (`date.today() + timedelta(days=durasi)`).
  5. Panggil `lab.buat_transaksi(nim, daftar_kode, batas_tanggal)` di dalam blok `try-except`.
  6. Jika sukses, cetak nota/ringkasan transaksi (ID Transaksi, Nama Peminjam, Daftar Alat, Batas Waktu). Jika gagal, cetak pesan error.

---

### 🔹 Fitur 4: Tampilkan Semua Transaksi (`fitur_program/tampilkan_transaksi.py`)
* **Tujuan:** Melihat seluruh transaksi peminjaman yang pernah dilakukan.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Panggil `lab.tampilkan_transaksi()`.
  2. Cek apakah daftar kosong. Jika kosong, tampilkan pesan informatif.
  3. Lakukan perulangan (`for`) untuk setiap objek transaksi:
     - Tampilkan ID Transaksi, Nama & NIM Mahasiswa, Tanggal Pinjam, Batas Pengembalian, dan Status Transaksi (`DIPINJAM` / `SEBAGIAN_DIKEMBALIKAN` / `SELESAI`).
     - Lakukan iterasi pada `transaksi.daftar_item` untuk menampilkan rincian tiap alat beserta status kembalinya (sudah kembali/belum, tanggal, kondisi saat kembali).

---

### 🔹 Fitur 5: Proses Pengembalian Alat (`fitur_program/proses_pengembalian.py`)
* **Tujuan:** Memproses pengembalian unit alat perorangan (mendukung pengembalian bertahap/sebagian).
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Minta input `ID Transaksi` (misal `T001`).
  2. Validasi apakah ID transaksi ada di `lab.transaksi` dan pastikan transaksi masih aktif (`transaksi.masih_aktif()`).
  3. Tampilkan daftar alat yang **belum dikembalikan** pada transaksi tersebut (`transaksi.alat_belum_kembali()`).
  4. Minta input `kode_alat` yang ingin dikembalikan saat ini.
  5. Minta input kondisi alat saat dikembalikan (1. Baik, 2. Rusak Ringan, 3. Rusak Berat).
  6. Panggil `lab.proses_pengembalian(id_transaksi, kode_alat, kondisi)` di dalam blok `try-except`.
  7. Tampilkan status terbaru transaksi (apakah masih `SEBAGIAN_DIKEMBALIKAN` atau sudah `SELESAI`).

---

### 🔹 Fitur 6: Cari Transaksi Berdasarkan Mahasiswa (`fitur_program/cari_transaksi.py`)
* **Tujuan:** Menampilkan seluruh transaksi yang berkaitan dengan satu mahasiswa tertentu.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Minta input `NIM` mahasiswa.
  2. Cek apakah mahasiswa terdaftar di sistem.
  3. Panggil `lab.cari_transaksi_by_mahasiswa(nim)` untuk mendapatkan list transaksi milik mahasiswa tersebut.
  4. Tampilkan informasi mahasiswa (Nama, NIM, jumlah transaksi yang sedang aktif).
  5. Jika tidak ada transaksi, tampilkan pesan bahwa mahasiswa belum pernah meminjam.
  6. Jika ada, lakukan perulangan dan cetak rincian ID transaksi, status, tanggal, serta status item alat-alatnya.

---

### 🔹 Fitur 7: Tampilkan Alat yang Tersedia (`fitur_program/tampilkan_alat_tersedia.py`)
* **Tujuan:** Menampilkan seluruh unit alat yang siap dipinjam.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Panggil `lab.tampilkan_alat_tersedia()`.
  2. Cek apakah ada alat yang tersedia.
  3. Tampilkan dalam format tabel yang rapi (Kolom: Kode Alat, Nama Alat, Kategori, Kondisi).
  4. Tampilkan total jumlah unit yang tersedia di bagian bawah tabel.

---

### 🔹 Fitur 8: Tampilkan Alat yang Sedang Dipinjam (`fitur_program/tampilkan_alat_dipinjam.py`)
* **Tujuan:** Menampilkan seluruh unit alat yang sedang dibawa oleh mahasiswa.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Panggil `lab.tampilkan_alat_dipinjam()`.
  2. Cek apakah ada alat yang sedang dipinjam.
  3. Tampilkan dalam format tabel yang rapi (Kolom: Kode Alat, Nama Alat, Kategori, Status).
  4. Tampilkan total unit yang sedang dipinjam.

---

### 🔹 Fitur 9: Tampilkan Alat yang Rusak (`fitur_program/tampilkan_alat_rusak.py`)
* **Tujuan:** Menampilkan daftar alat yang memerlukan perbaikan/pemeliharaan.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Panggil `lab.tampilkan_alat_rusak()`.
  2. Jika kosong, berikan pesan positif bahwa seluruh peralatan dalam kondisi baik.
  3. Jika ada, cetak tabel berisi Kode Alat, Nama, Kategori, dan Kondisi detailnya (`RUSAK_RINGAN` atau `RUSAK_BERAT`).

---

### 🔹 Fitur 10: Tampilkan Riwayat Peminjaman Mahasiswa (`fitur_program/riwayat_mahasiswa.py`)
* **Tujuan:** Melihat riwayat rekam jejak peminjaman mahasiswa dari awal hingga selesai.
* **Langkah-Langkah yang Perlu Dibuat:**
  1. Minta input `NIM` mahasiswa.
  2. Panggil `lab.riwayat_mahasiswa(nim)` di dalam blok `try-except`.
  3. Tampilkan data profil mahasiswa dan rekapitulasi riwayat peminjaman masa lalu beserta status akhir alat saat dikembalikan.

---

## 4. Cara Menjalankan dan Menguji Program

Setelah mengisi logika pada file fitur masing-masing, jalankan program dari terminal:

```bash
python main.py
```
