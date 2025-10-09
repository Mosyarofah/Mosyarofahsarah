class Pelanggan:
    def __init__(self, nama, email):
        self.nama = nama  # Menyimpan nama pelanggan
        self.email = email  # Menyimpan email pelanggan
        self.keranjang = Keranjang()  # Setiap pelanggan memiliki keranjang sendiri (composition)
        self.riwayat_pesanan = []  # List untuk menyimpan semua pesanan yang pernah dibuat
        # Implementasi: inisialisasi pelanggan dengan keranjang dan riwayat pesanan

    def buat_pesanan(self):
        pesanan = Pesanan(self)  # Membuat objek pesanan dari isi keranjang
        self.riwayat_pesanan.append(pesanan)  # Menyimpan pesanan ke riwayat
        self.keranjang = Keranjang()  # Keranjang dikosongkan (reset)
        return pesanan  # Mengembalikan objek pesanan
        # Implementasi: buat pesanan dari keranjang
     
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama  # Menyimpan nama produk
        self.harga = harga  # Harga satuan produk
        self.stok = stok  # Jumlah stok yang tersedia
        # Implementasi: inisialisasi produk
        


class Keranjang:
    def __init__(self):
        self.items = []  # List tuple (produk, jumlah) yang akan dibeli
        # Implementasi: inisialisasi keranjang kosong
       

    def tambah_produk(self, produk, jumlah):
        if produk.stok >= jumlah:  # Cek apakah stok cukup
            self.items.append((produk, jumlah))  # Tambahkan produk dan jumlah ke keranjang
            print(f"{jumlah}x {produk.nama} ditambahkan ke keranjang.")  # Info berhasil
        else:
            print(f"Stok tidak mencukupi untuk produk '{produk.nama}'.")  # Info gagal
        # Implementasi: tambahkan produk ke keranjang
        


class Pesanan:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan  # Menyimpan objek pelanggan (composition)
        self.items = []  # List item pesanan
        for produk, jumlah in pelanggan.keranjang.items:
            produk.stok -= jumlah  # Kurangi stok produk sesuai jumlah
            item = ItemPesanan(produk, jumlah)  # Buat item pesanan dari produk
            self.items.append(item)  # Tambahkan item ke pesanan
        # Implementasi: inisialisasi pesanan
      

class ItemPesanan:
    def __init__(self, produk, jumlah):
        self.produk = produk  # Menyimpan referensi ke produk (association)
        self.jumlah = jumlah  # Jumlah produk yang dipesan
        # Implementasi: inisialisasi item pesanan
                                                                                                                                                                                    

    def total_harga(self):    
        return self.produk.harga * self.jumlah  # Hitung total harga item (harga x jumlah)


# 1. Membuat beberapa produk
p1 = Produk("Laptop", 8000000, 5)
p2 = Produk("Mouse", 150000, 10)
p3 = Produk("Keyboard", 300000, 7)

# 2. Membuat pelanggan
pelanggan = Pelanggan("Mosya Rofah", "mosya@example.com")

# 3. Menambah produk ke keranjang pelanggan
pelanggan.keranjang.tambah_produk(p1, 1)
pelanggan.keranjang.tambah_produk(p2, 2)
pelanggan.keranjang.tambah_produk(p3, 1)

# 4. Membuat pesanan dari keranjang
pesanan = pelanggan.buat_pesanan()

# 5. Menampilkan detail pesanan dan total harga (di luar class)
print(f"\nPesanan untuk {pesanan.pelanggan.nama}:")
total = 0
for item in pesanan.items:
   subtotal = item.total_harga()
   print(f"- {item.jumlah}x {item.produk.nama} {item.produk.harga} = {subtotal}")
   total += subtotal
print(f"Total Harga: {total}")