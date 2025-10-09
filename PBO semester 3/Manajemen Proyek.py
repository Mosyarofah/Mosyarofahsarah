class Perusahaan:
    def __init__(self, nama):
        self.nama = nama
        self.proyek = []
        self.tim = []

    def buat_proyek(self, nama_proyek, deskripsi):
        proyek_baru = Proyek(nama_proyek, deskripsi)
        self.proyek.append(proyek_baru)
        print(f"Proyek '{nama_proyek}' berhasil dibuat.")
        return proyek_baru

    def buat_tim(self, nama_tim):
        tim_baru = Tim(nama_tim)
        self.tim.append(tim_baru)
        print(f"Tim '{nama_tim}' berhasil dibuat.")
        return tim_baru


class Proyek:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi
        self.tugas = []

    def tambah_tugas(self, deskripsi_tugas):
        tugas_baru = Tugas(deskripsi_tugas)
        self.tugas.append(tugas_baru)
        print(f"Tugas '{deskripsi_tugas}' berhasil ditambahkan ke proyek '{self.nama}'.")
        return tugas_baru


class Tim:
    def __init__(self, nama):
        self.nama = nama
        self.developer = []

    def tambah_developer(self, developer):
        self.developer.append(developer)
        print(f"Developer '{developer.nama}' ditambahkan ke tim '{self.nama}'.")


class Developer:
    def __init__(self, nama, keahlian):
        self.nama = nama
        self.keahlian = keahlian


class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.developer = None

    def tugaskan_ke(self, developer):
        self.developer = developer
        print(f"Tugas '{self.deskripsi}' telah ditugaskan ke {developer.nama} ({developer.keahlian}).")


if __name__ == "__main__":
    perusahaan = Perusahaan("Jayalah")

    tim_backend = perusahaan.buat_tim("Backend Team")

    dev1 = Developer("musya", "Backend Developer")
    dev2 = Developer("vanessa", "Database Engineer")

    tim_backend.tambah_developer(dev1)
    tim_backend.tambah_developer(dev2)

    proyek1 = perusahaan.buat_proyek("Sistem Inventori", "Aplikasi untuk manajemen stok barang")

    tugas1 = proyek1.tambah_tugas("Desain struktur database")
    tugas2 = proyek1.tambah_tugas("Implementasi API produk")

    tugas1.tugaskan_ke(dev2)
    tugas2.tugaskan_ke(dev1)
