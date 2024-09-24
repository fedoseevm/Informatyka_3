import math


def IfPrime(x):
    for i in range(2, round(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

plik = open('liczby2.txt', 'r')
numbers = list(map(int, plik.read().split()))
plik.close()

print(numbers)

wynik = []
min_suma_dzielnikow_pierwszych = max(numbers)
for number in numbers:
    suma_dzielnikow_pierwszych = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0 and IfPrime(i):
            suma_dzielnikow_pierwszych += i
    if min_suma_dzielnikow_pierwszych > suma_dzielnikow_pierwszych:
        wynik = number
        min_suma_dzielnikow_pierwszych = suma_dzielnikow_pierwszych



print(wynik)
