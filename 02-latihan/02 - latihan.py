userInput = float(input("Masukkan angka :"))

lebihdari = userInput > 8
print("Angka yang anda masukkan :", lebihdari)

lebih_dari = userInput > 13
print("Angka yang anda masukkan :", lebih_dari)

kurangdari = userInput < 5
print("Angka yang anda masukkan :", kurangdari)

kurang_dari = userInput < 11
print("Angka yang anda masukkan :", kurang_dari)

irisan = kurangdari or (lebihdari and kurang_dari) or lebih_dari
print("Angka yang anda masukkan :", irisan)

a = 0b00000111
print("nilai dari", a ,"adalah :", format(a,'08b'))

b = 0b00000100
print("nilai dari", b ,"adalah :", format(b,'08b'))

atau = a|b
print("nilai dari", atau ,"adalah :", format(atau,'08b'))

c = 6
print("nilai dari", c ,"adalah:" ,format(c,'08b'))

d = ~c
print("nilai dari", d, "adalah:" ,format(d,'08b'))

e = 0b00010010
f = 0b11111111
print("nilai dari", e^f, "adalah:" ,format(e^f,'08b'))


