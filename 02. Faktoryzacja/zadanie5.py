import math


def CzyZlozona(x):
    for i in range(2, round(math.sqrt(x) + 1)):
        if x % i == 0:
            return True
    return False

def SumaCyfr(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //= 10
    return suma

def SumaCyfrCzynnikow(x):
    suma = 0
    czynnik = 2
    while x > 1:
        while x % czynnik == 0:
            suma += SumaCyfr(czynnik)
            x /= czynnik
        czynnik += 1
    return suma

n = int(input("Podaj liczbę naturalną większą od 1: "))
if n < 1:
    print("Podaj liczbę większą od 1")

if CzyZlozona(n) and SumaCyfr(n) == SumaCyfrCzynnikow(n):
    print("Liczba Smitha!")
else:
    print("Nie jest liczbą Smitha")
