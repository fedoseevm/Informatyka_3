import math

def ifPrime(x):
    if x < 2:
        return False
    for i in range(2, round(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

n = int(input("Podaj liczbę: "))
for i in range(2, n + 1):
    if n % i == 0 and ifPrime(i):
        print(i)