file = open("dane.txt", "r")
numbers = list(map(int, file.read().split()))
file.close()

wynik = ""
ilosc_liczb = 0
for i in numbers:
    ilosc_dzielnikow = 1
    for j in range(2, i//2 + 1):
        if (i % j == 0):
            ilosc_dzielnikow += 1
        if (ilosc_dzielnikow > 2):
            wynik += str(i) + " "
            ilosc_liczb += 1
            break
print(wynik)
print(ilosc_liczb)

