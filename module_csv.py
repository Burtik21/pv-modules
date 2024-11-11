import csv

# Čtení z CSV
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Zápis do CSV
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 23])
