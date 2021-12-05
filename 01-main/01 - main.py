print("Hello world")
a = 10
print(a)
b = complex(0,2)
print(b)
print(b, "adalah ", type(b))

from ctypes import c_double
c = c_double(23.12322)
print(c, "adalah ", type(c))

d = 23.12322
print(d, "adalah ", type(d))

e = int(d)
print(e)

nama = input("Masukkan nama : ")
NIM = int(input("Masukkan NIM : "))
Kelas = input("Masukkan kelas : ")
print("Nama :", nama)
print("NIM : ", NIM)
print("Kelas : ", Kelas)