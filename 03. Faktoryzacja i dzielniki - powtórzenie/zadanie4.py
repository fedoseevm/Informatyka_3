import math


def IfPrime(x):
    for i in range(2, round(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

plik = open('liczby2.txt', 'r')
numbers = list(map(int, plik.read().split()))
plik.close()

print(numbers)

max_ilosc_dzielnikow_pierwszych = 0
for i in range(len(numbers)):
    ilosc_dzielnikow_pierwszych = 0
    for j in range(1, numbers[i] // 2 + 1):
        if IfPrime(j):
            ilosc_dzielnikow_pierwszych += 1
