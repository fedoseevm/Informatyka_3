def BinarySearch(T, a, n):
    lewy = 0
    prawy = n - 1
    while lewy < prawy:
        srodek = (lewy + prawy) // 2
        if T[srodek] == a:
            return True
        elif T[srodek] < a:
            lewy = srodek + 1
        else:
            prawy = srodek
    return T[lewy] == a


with open("ciagi.txt", "r") as plik:
    a = int(plik.readline().rstrip())
    for line in plik:
        ciag = list(map(int, line.split()))
        if BinarySearch(ciag, a, len(ciag)):
            print(ciag)
