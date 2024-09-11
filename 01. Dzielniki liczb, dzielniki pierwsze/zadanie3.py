n = int(input("Podaj liczbę: "))
suma = n
for i in range(1, n // 2 + 1):
    if n % i == 0:
        suma += i
print(suma)