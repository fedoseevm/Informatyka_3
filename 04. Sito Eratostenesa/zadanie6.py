def SitoEratostenesa(n):
    primeList = [True] * (n + 1)
    primeList[0] = False
    primeList[1] = False

    p = 2
    while p * p <= len(primeList):
        if primeList[p]:
            for i in range(p * p, len(primeList), p):
                primeList[i] = False
        p += 1
    return primeList


primeList = SitoEratostenesa(1000)
with open("ciag.txt") as file:
    numbers = list(map(int, file.read().split()))

amountOfPrimes = 0
for number in numbers:
    if primeList[number]:
        amountOfPrimes += 1
percentage = round(amountOfPrimes / len(numbers) * 100, 1)
print("Ilość liczb pierwszych w pliku ciag.txt: " + str(amountOfPrimes))
print(f"Co jest {percentage}% od wszystkich liczb")
