import csv
import pandas as pd

# membuka file csv dengan module csv
contacts = []

with open('data1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        contacts.append(row)

labels = contacts.pop(0)

print(f'{labels[0]}\t {labels[1]} \t {labels[2]}')
print('-'*34)
for row in contacts:
    print(f'{row[0]}\t {row[1]} \t {row[2]}')

# membuka file csv dengan pandas

df = pd.read_csv('data1.csv')
print(df)

