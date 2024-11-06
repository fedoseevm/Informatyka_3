def SumaCyfr(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //= 10
    return suma

file = open("dane.txt", "r")
numbers = list(map(int, file.read().split()))
file.close()

suma_cyfr_czynnikow = 0
for number in numbers:
    czynnik = 2
    while number > 1:
        while number % czynnik == 0:
            print(f"{czynnik} {SumaCyfr(czynnik)}")
            suma_cyfr_czynnikow += SumaCyfr(czynnik)
            number /= czynnik
        czynnik += 1
print(suma_cyfr_czynnikow)