import math


def IfPrime(x):
    if x == 1:
        return False
    for i in range(2, round(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

n = int(input("Podaj liczbę naturalną większą od 1: "))
if n < 1:
    print("Podaj liczbę większą od 1")

czynnik = 2
suma_czynnikow = 0
while n > 1:
    while n % czynnik == 0:
        suma_czynnikow += czynnik
        n /= czynnik
    czynnik += 1
if IfPrime(suma_czynnikow):
    print("tak")
else:
    print("nie")