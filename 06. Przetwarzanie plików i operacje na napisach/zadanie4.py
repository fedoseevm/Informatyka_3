with open("ciagi.txt", "r") as plik:
    liczba_ciagow = int(plik.readline().rstrip())
    ilosc_ciagow_parz = 0
    for i in range(liczba_ciagow - 1):
        linia = plik.readline().rstrip().split()
        if sum(linia[1:]) % 2 == 0:
            liczba_ciagow += 1