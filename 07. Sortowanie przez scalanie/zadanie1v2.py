def scal(T1, T2):
    wynik = []
    n1 = len(T1)
    n2 = len(T2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if T1[i] < T2[j]:
            wynik.append(T1[i])
            i += 1
        else:
            wynik.append(T2[j])
            j += 1

    wynik.extend(T1[i:])
    wynik.extend(T2[j:])
    return wynik


def sort(T):
    n = len(T)
    if n == 1:
        return T
    srodek = (n - 1) // 2
    lewy = sort(T[:srodek+1])
    prawy = sort(T[srodek+1:])
    return scal(lewy, prawy)

ciag = input("Podaj ciąg: ")
T = list(map(int, ciag.split()))
print(T)
T = sort(T)
print(T)
