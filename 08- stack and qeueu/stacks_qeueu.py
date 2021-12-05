from collections import deque

# stacks atau tumpukkan
tumpukan = [1,2,3,4,5,6]
print("Data sekarang", tumpukan)

tumpukan.append(7)
print("Data masuk :",7)
print("Data sekarang", tumpukan)

tumpukan.append(8)
print("Data masuk :",8)
print("Data sekarang", tumpukan)

x = tumpukan.pop()
print("Data keluar :",x)
print("Data sekarang", tumpukan)

print("="*50)
# qeueu atau antrian
antrian = deque([1,2,3,4,5,6])
print("Data sekarang", antrian)

antrian.append(7)
print("Data masuk :",7)
print("Data sekarang", antrian)

antrian.append(8)
print("Data masuk :",8)
print("Data sekarang", antrian)

x = antrian.popleft()
print("Data keluar :",x)
print("Data sekarang", antrian)
