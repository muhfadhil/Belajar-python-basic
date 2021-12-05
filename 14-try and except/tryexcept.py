false = 3
while True:
    try:
        angka = int(input("Masukkan angka : "))
        if angka % 2 == 0:
            print("Bilangan Genap")
        else:
            print("Bilangan Ganjil")
    except:
        false -= 1
        print("Yang Anda masukkan bukan angka\nKesempatan",false,"kali salah lagi")

        if false == 0:
            print("Salah tiga kali")
            break
        
print("Byeeeeeeeeeeeeee")