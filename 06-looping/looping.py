# while loop
start = True
angka = 0

while start:
    print(angka," salah")
    if angka == 5:
        print("Nilai ditemukan")
        start = False
    angka += 1

# for loop
nama = ['tasya','fadhil','dimas','caca']
for i in range(1,10):
    print(i)

for p in nama:
    if 'tasya' in nama:
        print('data benar')
    else:
        print('data salah')
    break

