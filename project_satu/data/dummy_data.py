"""
Modul Dummy Data / Seeder untuk Inisialisasi Data Awal Laboratorium
"""
from datetime import date, timedelta
from typing import TYPE_CHECKING

from models.enums import KondisiAlat

if TYPE_CHECKING:
    from services.lab_manager import LabManager


def inisialisasi_dummy_data(lab: 'LabManager') -> None:
    """Mengisikan data awal mahasiswa, peralatan, dan contoh transaksi ke dalam LabManager."""

    # ==================== 1. DUMMY DATA MAHASISWA (6 Mahasiswa) ====================
    daftar_mhs = [
        ("M001", "Andi Pratama", "081234567801"),
        ("M002", "Budi Santoso", "081234567802"),
        ("M003", "Citra Lestari", "081234567803"),
        ("M004", "Dewi Anggraini", "081234567804"),
        ("M005", "Eko Prasetyo", "081234567805"),
        ("M006", "Fajar Hidayat", "081234567806"),
    ]
    for nim, nama, hp in daftar_mhs:
        lab.tambah_mahasiswa(nim, nama, hp)

    # ==================== 2. DUMMY DATA PERALATAN (10 Unit Alat) ====================
    daftar_alat = [
        ("ALT-001", "Multimeter Digital Fluke", "Elektronika", KondisiAlat.BAIK),
        ("ALT-002", "Oscilloscope Rigol", "Elektronika", KondisiAlat.BAIK),
        ("ALT-003", "Crimping Tool RJ45", "Jaringan", KondisiAlat.BAIK),
        ("ALT-004", "LAN Tester Pro", "Jaringan", KondisiAlat.BAIK),
        ("ALT-005", "Switch Cisco 24-Port", "Jaringan", KondisiAlat.BAIK),
        ("ALT-006", "Solder Station Hakko", "Elektronika", KondisiAlat.RUSAK_RINGAN),
        ("ALT-007", "Kamera DSLR Canon 80D", "Multimedia", KondisiAlat.BAIK),
        ("ALT-008", "Tripod Kamera Takara", "Multimedia", KondisiAlat.BAIK),
        ("ALT-009", "Power Supply DC GW Instek", "Elektronika", KondisiAlat.RUSAK_BERAT),
        ("ALT-010", "Raspberry Pi 4 Model B", "Komputasi", KondisiAlat.BAIK),
    ]
    for kode, nama, kategori, kondisi in daftar_alat:
        lab.tambah_alat(kode, nama, kategori, kondisi)

    # ==================== 3. DUMMY TRANSAKSI PEMINJAMAN ====================
    # Transaksi 1: Peminjaman aktif (M001 meminjam ALT-001 dan ALT-002) -> Status: DIPINJAM
    batas_1 = date.today() + timedelta(days=5)
    lab.buat_transaksi("M001", ["ALT-001", "ALT-002"], batas_1)

    # Transaksi 2: Peminjaman dengan pengembalian sebagian (M002 meminjam ALT-003 dan ALT-004, ALT-003 sudah dikembalikan)
    batas_2 = date.today() + timedelta(days=7)
    trx2 = lab.buat_transaksi("M002", ["ALT-003", "ALT-004"], batas_2)
    lab.proses_pengembalian(trx2.id_transaksi, "ALT-003", KondisiAlat.BAIK)
    # Status trx2 otomatis: SEBAGIAN_DIKEMBALIKAN (ALT-004 masih dipinjam)
