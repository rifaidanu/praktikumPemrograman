from enum import Enum


class StatusTransaksi(Enum):
    """Status kondisi sebuah transaksi peminjaman."""
    DIPINJAM = "dipinjam"
    SEBAGIAN_DIKEMBALIKAN = "sebagian dikembalikan"
    SELESAI = "selesai"


class KondisiAlat(Enum):
    """Kondisi fisik unit alat laboratorium."""
    BAIK = "baik"
    RUSAK_RINGAN = "rusak ringan"
    RUSAK_BERAT = "rusak berat"


class StatusAlat(Enum):
    """Status ketersediaan unit alat untuk dipinjam."""
    TERSEDIA = "tersedia"
    DIPINJAM = "dipinjam"
    TIDAK_TERSEDIA = "tidak tersedia"
