import tkinter

tampilan = tkinter.Tk()

def tekan():
    label2 = tkinter.Label(tampilan, text="Good job!")
    label2.pack()

label = tkinter.Label(tampilan,text="Hallo nama saya Muhammad Fadhil")
tombol = tkinter.Button(tampilan, text="Tekan aku", command=tekan)

label.pack()
tombol.pack()
tampilan.mainloop()