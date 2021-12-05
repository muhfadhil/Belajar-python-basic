print("PROGRAM KONVERSI TEMPERATUR")

print("====CELCIUS====")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah", celcius, "celcius")

reamur = (4/5)*celcius
print("suhu adalah", reamur, "reamur")

fahrenheit = ((9/5)*celcius) + 32
print("suhu adalah", fahrenheit, "fahrenheit")

kelvin = celcius + 273
print("suhu adalah", kelvin, "kelvin")

print("====REAMUR====")

reamur = float(input('Masukkan suhu dalam reamur : '))
print("suhu adalah", reamur, "reamur")

celcius = (5/4)*reamur
print("suhu adalah", celcius, "celcius")

fahrenheit = ((9/4)*reamur) + 32
print("suhu adalah", fahrenheit, "fahrenheit")

kelvin = ((5/4)*reamur) + 273
print("suhu adalah", kelvin, "kelvin")

print("====FAHRENHEIT====")

fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
print("suhu adalah", fahrenheit, "fahrenheit")

celcius = (5/9)*(fahrenheit-32)
print("suhu adalah", celcius, "celcius")

reamur = (4/9)*(fahrenheit-32)
print("suhu adalah", reamur, "reamur")

kelvin = ((5/9)*(fahrenheit-32) + 273)
print("suhu adalah", kelvin, "kelvin")

print("====KELVIN====")

kelvin = float(input('Masukkan suhu dalam kelvin : '))
print("suhu adalah", kelvin, "kelvin")

celcius = kelvin - 273
print("suhu adalah", celcius, "celcius")

reamur = (4/5)*(kelvin - 273)
print("suhu adalah", reamur, "reamur")

fahrenheit = ((9/5)*(kelvin - 273)) + 32
print("suhu adalah", fahrenheit, "fahrenheit")