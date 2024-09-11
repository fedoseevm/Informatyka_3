n = int(input("Podaj liczbę: "))
ilosc_dzielnikow = 2 # 1 i sama liczba
for i in range(2, n // 2 + 1):
    if n % i == 0:
        ilosc_dzielnikow += 1
print(ilosc_dzielnikow)