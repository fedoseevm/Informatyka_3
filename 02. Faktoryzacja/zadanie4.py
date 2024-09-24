n = int(input("Podaj liczbę naturalną większą od 1: "))
if n < 1:
    print("Podaj liczbę większą od 1")

czynnik = 2
ilosc_roznych_czynnikow = 0
while n > 1:
    if n % czynnik == 0:
        ilosc_roznych_czynnikow += 1
    while n % czynnik == 0:
        n /= czynnik
    czynnik += 1

print(ilosc_roznych_czynnikow)