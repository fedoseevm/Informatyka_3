n = int(input("Podaj liczbę: "))
suma_dzielnikow = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        suma_dzielnikow += i
if n == suma_dzielnikow:
    print("tak")
else:
    print("nie")