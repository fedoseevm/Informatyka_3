def SumaCyfr(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //= 10
    return suma

plik = open('liczby2.txt', 'r')
numbers = list(map(int, plik.read().split()))
plik.close()

print(numbers)

min_suma_cyfr_czynnikow = max(numbers)
wynik = 0
for number in numbers:
    suma_cyfr_czynnikow = 0
    czynnik = 2
    temp_number = number
    while temp_number > 1:
        while temp_number % czynnik == 0:
            suma_cyfr_czynnikow += SumaCyfr(czynnik)
            temp_number //= czynnik
        czynnik += 1
    if min_suma_cyfr_czynnikow > suma_cyfr_czynnikow:
        min_suma_cyfr_czynnikow = suma_cyfr_czynnikow
        wynik = number
print(wynik)