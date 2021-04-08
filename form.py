class Form():
    # contructor
    def __init__(self, nama, telp, jumlah, jenis, kertas, cover, gambar):
        self.nama = nama
        self.telp = telp
        self.jumlah = jumlah
        self.jenis = jenis
        self.kertas = kertas
        self.cover = cover
        self.gambar = gambar

    # nama
    def get_nama(self):
        return self.nama

    # telp
    def get_telp(self):
        return self.telp

    # jumlah
    def get_jumlah(self):
        return self.jumlah

    # jenis
    def get_jenis(self):
        return self.jenis

    # cover
    def get_cover(self):
        return self.cover

    # kertas
    def get_kertas(self):
        return self.kertas

    # gambar
    def get_gambar(self):
        return self.gambar
