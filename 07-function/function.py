
cowo = ['Dimas','Raid','Fadhil','Alken']
cewe = ['Caca','Adel','Marel','Cinda','Dilla']
grup = [cowo,cewe]

for anggota in grup:
    print(anggota)
    for anggota2 in anggota:
        print(anggota2)
nama = input('Masukkan nama : ')

def gender(nama):  
    global grup,cowo,cewe
    gender1 = 'laki-laki'
    gender2 = 'perempuan'
    
    if nama in cowo:
        print('Anggota bergender :', gender1)
    elif nama in cewe:
        print('Anggota bergender :', gender2)
    else:
        print('nama yang Anda masukkan salah')
    return nama

gender(nama)

# fungsi mengurutkan angka
angka = input("masukkan angka : ")
def urutAngka(listAngka):
    # 2 3 5 2 5 
    return sorted(list(map(int, listAngka.split(' '))))

print(urutAngka(angka))