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
print(suma_czynnikow)