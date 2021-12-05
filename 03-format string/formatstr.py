a = "Tasya"
b = "Nur"
c = "Taffana"
nama_lengkap = a + ' '+ b + ' ' + c
print(nama_lengkap)

# panjang string
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " adalah " + str(panjang))

pisah = nama_lengkap.split(' ')
print(pisah)
gabung = ' '.join(pisah)
print(gabung)

# index string
print("Index ke-1 dari " + nama_lengkap + " adalah " + nama_lengkap[1])
print("Index ke-6 dari " + nama_lengkap + " adalah " + nama_lengkap[6])
print("Index ke-2:5 dari " + nama_lengkap + " adalah " + nama_lengkap[2:6]+ "'")
print("Index 2,4,6,8,10 dari " + nama_lengkap + " adalah " + nama_lengkap[2:11:2])

lower = nama_lengkap.islower()
print(lower)
lower = nama_lengkap.lower()
print(lower)

upper = nama_lengkap.upper()
print(upper)

# rjust, ljust dan center
center = 'center'.center(20,'=')
print(center)

kanan = 'kanan'.rjust(20,';')
print(kanan)

kiri = 'kiri'.ljust(20,';')
print(kiri)

# strip
tengah = center.strip()
print(tengah)

nama = "taffana"
nama_lengkap = f"tasya nur {nama}"
print(nama_lengkap)

angka = 2021
print(f"sekarang tahun {angka:+d}")

ribuan = 2500000
print(f"ribuan adalah Rp {ribuan:,}")

boolean = False
print(f"nilai boolean adalah {boolean}")

desimal = 1234.234213
print(f"Nilai desimal adalah {desimal:.2f}")

persen = 0.10
format_persen = f"Persentase = {persen:.1%}"
print(format_persen)