import random

with open("losowe.txt", "w") as plik:
    for i in range(10):
        plik.write(str(random.randint(1, 100)) + "\n")

suma = 0
minimum = 100
maximum = 0
avg = 0
with open("losowe.txt", "r") as plik:
    for line in plik:
        liczba = int(line.rstrip())
        suma += liczba
        if minimum > liczba:
            minimum = liczba
        if maximum < liczba:
            maximum = liczba
avg = suma / 10

print("Suma = " + str(suma))
print("Minimum: " + str(minimum))
print("Maximum: " + str(maximum))
print("Srednia = " + str(avg))