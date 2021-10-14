import csv
from faker import Faker

fake = Faker('pt_BR')

header = ['name']
data = []

for _ in range(10):
    data.append([f'{fake.name()}'])

with open('files/1_milhao.csv', 'w+', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(data)
