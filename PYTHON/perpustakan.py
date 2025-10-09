from datetime import date  # Untuk mendapatkan tanggal hari ini

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama  # Menyimpan nama perpustakaan
        self.koleksi_buku = []  # Menyimpan list buku yang tersedia
        self.daftar_anggota_list = []  # Menyimpan list anggota yang terdaftar
        self.riwayat_peminjaman = []  # Menyimpan list riwayat peminjaman

    def daftar_anggota(self, anggota):
        self.daftar_anggota_list.append(anggota)  # Tambahkan objek anggota ke daftar
        print(f"Anggota '{anggota.nama}' berhasil didaftarkan.")  # Tampilkan pesan sukses

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)  # Tambahkan objek buku ke koleksi
        print(f"Buku '{buku.judul}' oleh {buku.penulis} berhasil ditambahkan ke koleksi.")  # Tampilkan pesan sukses

    def pinjam_buku(self, anggota, buku):
        # Cek apakah buku ada di koleksi dan belum dipinjam
        if buku in self.koleksi_buku and not buku.dipinjam:
            buku.dipinjam = True  # Tandai buku sebagai sedang dipinjam
            anggota.buku_dipinjam.append(buku)  # Tambahkan ke daftar pinjaman milik anggota
            peminjaman = Peminjaman(anggota, buku, date.today())  # Buat objek peminjaman dengan tanggal hari ini
            self.riwayat_peminjaman.append(peminjaman)  # Tambahkan ke riwayat peminjaman
            print(f"Buku '{buku.judul}' dipinjam oleh {anggota.nama} pada {peminjaman.tanggal_pinjam}.")  # Tampilkan info peminjaman
        else:
            print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")  # Tampilkan pesan jika gagal dipinjam

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul  # Simpan judul buku
        self.penulis = penulis  # Simpan nama penulis
        self.dipinjam = False  # Status peminjaman (default: False / belum dipinjam)

class Anggota:
    def __init__(self, nama):
        self.nama = nama  # Simpan nama anggota
        self.buku_dipinjam = []  # List buku yang sedang dipinjam anggota

class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        self.anggota = anggota  # Simpan objek anggota
        self.buku = buku  # Simpan objek buku
        self.tanggal_pinjam = tanggal_pinjam  # Simpan tanggal saat buku dipinjam

# ======================
# CONTOH PENGGUNAAN
# ======================

# Buat objek perpustakaan
perpus = Perpustakaan("Perpustakaan Kota")  # Inisialisasi objek perpustakaan dengan nama

# Buat objek buku
b1 = Buku("Laskar Pelangi", "Andrea Hirata")  # Buku pertama
b2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")  # Buku kedua

# Buat objek anggota
a1 = Anggota("MosyaRofah")  # Anggota pertama
a2 = Anggota("Khoirum Nurfatikha A")  # Anggota kedua

# Tambahkan buku ke perpustakaan
perpus.tambah_buku(b1)  # Tambahkan buku pertama ke koleksi
perpus.tambah_buku(b2)  # Tambahkan buku kedua ke koleksi

# Daftarkan anggota ke perpustakaan
perpus.daftar_anggota(a1)  # Daftarkan anggota pertama
perpus.daftar_anggota(a2)  # Daftarkan anggota kedua

# Debug: Tampilkan semua anggota yang terdaftar
print("\n[DEBUG] Daftar Semua Anggota Terdaftar:")  # Judul debug output
for anggota in perpus.daftar_anggota_list:
    print(f"- {anggota.nama}")  # Tampilkan nama setiap anggota

# Proses peminjaman buku
perpus.pinjam_buku(a1, b1)  # Anggota 1 meminjam buku 1 (berhasil)
perpus.pinjam_buku(a2, b1)  # Anggota 2 mencoba meminjam buku 1 (gagal karena sudah dipinjam)
perpus.pinjam_buku(a2, b2)  # Anggota 2 meminjam buku 2 (berhasil)

# Tampilkan status semua peminjaman
print("\nStatus Peminjaman:")  # Judul output
for p in perpus.riwayat_peminjaman:
    # Tampilkan siapa meminjam buku apa dan kapan
    print(f"{p.anggota.nama} meminjam '{p.buku.judul}' pada {p.tanggal_pinjam}")
