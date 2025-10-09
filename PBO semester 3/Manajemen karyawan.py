


class Karyawan:
    # Constructor (__init__) untuk menginisialisasi atribut karyawan
    def __init__(self, nama, id_karyawan, gaji_pokok):
        # self.nama digunakan untuk menyimpan nama karyawan
        self.nama = nama
        # self.id_karyawan menyimpan ID unik dari karyawan
        self.id_karyawan = id_karyawan
        # self.gaji_pokok menyimpan nilai gaji pokok karyawan
        self.gaji_pokok = gaji_pokok

    # Method untuk menghitung gaji karyawan (default hanya gaji pokok)
    def hitung_gaji(self):
        return self.gaji_pokok

    # Method untuk menampilkan informasi dasar karyawan
    def info(self):
        # f-string digunakan agar mudah menampilkan variabel di dalam teks
        return f"{self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


class Manager(Karyawan):
    # Constructor Manager menambah atribut baru yaitu tunjangan
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        # Memanggil constructor milik parent class (Karyawan)
        super().__init__(nama, id_karyawan, gaji_pokok)
        # Menambahkan atribut baru: tunjangan
        self.tunjangan = tunjangan

    # Method ini "meng-override" (menimpa) method dari parent class
    # Tujuannya agar perhitungan gaji menambahkan tunjangan
    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

    # Override juga method info() agar menampilkan teks "Manager"
    def info(self):
        return f"Manager : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


class Programmer(Karyawan):
    # Constructor Programmer menambah atribut baru yaitu bonus
    def __init__(self, nama, id_karyawan, gaji_pokok, bonus):
        # Memanggil constructor dari parent class (Karyawan)
        super().__init__(nama, id_karyawan, gaji_pokok)
        # Menambahkan atribut baru: bonus
        self.bonus = bonus

    # Override method hitung_gaji untuk menambah bonus ke gaji pokok
    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus

    # Override method info() agar menampilkan teks "Programmer"
    def info(self):
        return f"Programmer : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# ================================================================
# Bagian utama program (Main Program)
# ================================================================
if __name__ == "__main__":
    # Membuat objek dari class Manager dengan nama, ID, gaji pokok, dan tunjangan
    manager1 = Manager("Mosyarofah", "M001", 12000000, 3000000)

    # Membuat objek dari class Programmer dengan nama, ID, gaji pokok, dan bonus
    programmer1 = Programmer("Sarah", "P001", 10000000, 2000000)

    # Memanggil method info() dari masing-masing objek
    # Karena method info() di-override, hasilnya akan berbeda tiap class
    print(manager1.info())       # Menampilkan info Manager
    print(programmer1.info())    # Menampilkan info Programmer


