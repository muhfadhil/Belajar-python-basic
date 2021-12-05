# menulis file text
# cara pertama
data = "Hallo nama saya Muhammad fadhil"
file = open("text.txt",'w')
file.write(data)
file.close()

# cara kedua
data2 = "NIM saya 240199"
with open("text.txt",'w') as file2:
    file2.write(data2)
file2.close()

# membaca file text
file3 = open("text.txt",'r')
print(file3.read())
file3.close()

# menambah 
file4 = open("text.txt",'a')
file4.write("\nSalam kenal semuanya")
    
