# class
class mahasiswa():
    
    jumlah_mahasiswa = 0
    jurusan = "matematika"   # class variable  
    __nilai = 0 # private

    def __init__(self, input_name, input_NIM):
        self.name = input_name  # public
        self.nim = input_NIM   # public
        mahasiswa.jumlah_mahasiswa += 1

    def belajar(self, kondisi):
        print(self.name,'sedang belajar', kondisi)

    def tidur(self, tempat):
        print(self.name,'sedang tidur di', tempat)

    def uts(self, nilai):
        self.__nilai += nilai

    def uas(self, nilai):
        self.__nilai += nilai

    def penilaian(self):
        if self.__nilai > 80:
            print(self.name, "mendapatkan nilai A")
        elif 70 < self.__nilai <= 80:
            print(self.name, "mendapatkan nilai B")
        elif 60 < self.__nilai <= 70:
            print(self.name, "mendapatkan nilai C")
        elif 50 < self.__nilai <= 60:
            print(self.name, "mendapatkan nilai D")
        else:
            print(self.name, "tidak lulus")

class siswa(mahasiswa):  # inheritance

    jumlah_siswa = 0

    def __init__(self, input_name, input_absen, kelas):
        self.name = input_name  # public
        self.absen = input_absen   # public
        self.kelas = kelas
        siswa.jumlah_siswa += 1

# instance
fadhil = mahasiswa("Muhammad Fadhil", 24010)
dimas = mahasiswa("Dimas PP", 24010120)

print(fadhil.name)
print(fadhil.nim)
fadhil.belajar('dengan giat')
fadhil.tidur('kamar')

print("="*50)

fadhil.uts(50)
fadhil.uas(40)
fadhil.penilaian()
print(fadhil.jurusan)

print("="*50)

# menghitung jumlah mahasiswa
print(mahasiswa.jumlah_mahasiswa)

print("="*50)

safina = siswa("Safina",20, 5)
print(safina.name)
print(safina.absen)
print(safina.kelas)
safina.belajar('dengan rajin')

# menghitung jumlah siswa
print(siswa.jumlah_siswa)

safina.uts(60)
safina.uas(10)
safina.penilaian()