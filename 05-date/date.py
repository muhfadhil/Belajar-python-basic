import datetime as dt

print(" Kelahiran ".center(50,'='))

tanggal = int(input("Masukkan tanggal\t : "))
bulan = int(input("Masukkan bulan\t\t : "))
tahun = int(input("Masukkan tahun\t\t : "))
lahir = dt.date(tahun,bulan,tanggal)
print(f"Anda lahir pada {lahir}")

tanggal_lahir = f"Anda lahir pada hari {lahir:%A}"
print(tanggal_lahir)

hari_ini = dt.date.today()

umur_hari = hari_ini - lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30 
# print(umur_hari)

print(f"Umur Anda adalah {umur_tahun} tahun {umur_bulan} bulan")
print('\n')
print(" Jangka Waktu".center(50,'='))

hari_ini = dt.date.today()

tanggal = int(input("Masukkan tanggal\t : "))
bulan = int(input("Masukkan bulan\t\t : "))
tahun = int(input("Masukkan tahun\t\t : "))
hari = dt.date(tahun,bulan,tanggal)

jangka_waktu = hari - hari_ini
print(f"{hari} bersisa {jangka_waktu.days} hari lagi \nTepat pada hari {hari:%A}")

