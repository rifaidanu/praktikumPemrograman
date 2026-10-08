from .enums import KondisiAlat, StatusAlat


class Peralatan:
    """Mewakili satu unit fisik alat laboratorium dan mengelola kondisi serta ketersediaannya."""

    def __init__(
        self,
        kode_alat: str,
        nama: str,
        kategori: str,
        kondisi: KondisiAlat = KondisiAlat.BAIK
    ) -> None:
        self._kode_alat: str = kode_alat
        self._nama: str = nama
        self._kategori: str = kategori
        self._kondisi: KondisiAlat = kondisi
        self._status: StatusAlat = StatusAlat.TERSEDIA if kondisi == KondisiAlat.BAIK else StatusAlat.TIDAK_TERSEDIA

    @property
    def kode_alat(self) -> str:
        return self._kode_alat

    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, value: str) -> None:
        self._nama = value

    @property
    def kategori(self) -> str:
        return self._kategori

    @kategori.setter
    def kategori(self, value: str) -> None:
        self._kategori = value

    @property
    def kondisi(self) -> KondisiAlat:
        return self._kondisi

    @kondisi.setter
    def kondisi(self, value: KondisiAlat) -> None:
        self._kondisi = value

    @property
    def status(self) -> StatusAlat:
        return self._status

    @status.setter
    def status(self, value: StatusAlat) -> None:
        self._status = value

    def tersedia(self) -> bool:
        """True jika status alat saat ini adalah TERSEDIA."""
        return self._status == StatusAlat.TERSEDIA

    def sedang_dipinjam(self) -> bool:
        """True jika status alat saat ini adalah DIPINJAM."""
        return self._status == StatusAlat.DIPINJAM

    def tandai_dipinjam(self) -> None:
        """Mengubah status ketersediaan menjadi DIPINJAM."""
        self._status = StatusAlat.DIPINJAM

    def terima_kembali(self, kondisi: KondisiAlat) -> None:
        """Mencatat kondisi baru saat pengembalian dan memperbarui status ketersediaan."""
        self._kondisi = kondisi
        if kondisi == KondisiAlat.BAIK:
            self._status = StatusAlat.TERSEDIA
        else:
            self._status = StatusAlat.TIDAK_TERSEDIA

    def __repr__(self) -> str:
        return f"<Peralatan {self._kode_alat}: {self._nama} [{self._kondisi.value}, {self._status.value}]>"
