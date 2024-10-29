with open("ciagi.txt", "r") as plik:
    liczba_ciagow = int(plik.readline().rstrip())
    ilosc_ciagow_parz = 0
    for i in range(liczba_ciagow):
        linia = plik.readline().rstrip().split()
        # print(linia[1:])
        suma_elementow = sum(map(int, linia[1:]))
        # print(suma_elementow)
        # print(suma_elementow % 2)
        if suma_elementow % 2 == 0:
            ilosc_ciagow_parz += 1
            # print(ilosc_ciagow_parz)
print("Liczba ciagow z parzysta suma elementow: " + str(ilosc_ciagow_parz))
