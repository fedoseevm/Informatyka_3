import random

with open("losowe.txt", "w") as plik:
    for i in range(10):
        plik.write(str(random.randint(1, 100)) + "\n")

suma = 0
min = 0
max = 100
avg = 0
with open("losowe.txt", "r") as plik:
    for line in plik:
        suma += int(line)