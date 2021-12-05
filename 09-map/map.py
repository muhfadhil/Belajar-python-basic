# membuat map dengan x diketahui
x = [1,2,3,4,5,6]
print(x)
def square(x):
    return x**2

kuadrat = list(map(square,x))
print(kuadrat)
# zip method
zip_pasangan = zip(x,kuadrat)
pasangan = list(zip_pasangan)
print(pasangan)

print("="*60)

