import math


def ifPrime(x):
    if x < 2:
        return False
    for i in range(2, round(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

a, b = map(int, input("Podaj a i b: ").split())
if ifPrime(a) and ifPrime(b) and abs(a - b) == 2:
    print("Liczby bliźniacze")
else:
    print("Nie są liczbami bliźniaczymi")

