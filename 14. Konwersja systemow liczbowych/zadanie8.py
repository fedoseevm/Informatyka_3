import math


dec = float(input("Podaj liczbę dziesiętną: "))

calkowita = math.floor(dec)
ulamek = dec - calkowita
result = ""

while calkowita > 0:
    result = str(calkowita % 2) + result
    calkowita //= 2

result += ','

for _ in range(15):
    ulamek *= 2
    result += str(math.floor(ulamek))
    if ulamek > 1:
        ulamek -= 1
    elif ulamek == 1:
        break

result = result.rstrip('0')
print(result)