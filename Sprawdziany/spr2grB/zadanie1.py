def SitoEratostenesa(n):
    czy_pierwsza = [True] * (n + 1)
    czy_pierwsza[0] = False
    czy_pierwsza[1] = True

    p = 2
    while p * p <= n:
        if czy_pierwsza[p]:
            for i in range(p * p, n + 1, p):
                czy_pierwsza[i] = False
        p += 1

    wynik = []
    for i in range(2, n + 1):
        if czy_pierwsza[i]:
            wynik.append(i)
    return wynik


pierwsze = SitoEratostenesa(1000)

with open("liczby.txt", "r") as plik:
    liczby = list(map(int, plik.read().split()))

licznik = 0
for liczba in liczby:
    if liczba in pierwsze:
        licznik += 1

procent = licznik / len(liczby) * 100

print("Ile liczb w pliku liczby.txt jest liczbą pierwszą: ", licznik)
print(f"Stanowią {round(procent, 1)}% od wszystkich liczb")
