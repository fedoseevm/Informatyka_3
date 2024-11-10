from random import randint


# Napisz program w języku Python, który wylosuje milion liczb z zakresu od 1 do miliona, a następnie program zapisze ten ciąg posortowany metodą sortowania przez scalanie do pliku wyniki_3.txt (liczby w osobnych liniach).

def scal(T1, T2):
    result = []
    n1 = len(T1)
    n2 = len(T2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if T1[i] < T2[j]:
            result.append(T1[i])
            i += 1
        else:
            result.append(T2[j])
            j += 1
    result.extend(T1[i:])
    result.extend(T2[j:])
    return result

def sort(T):
    n = len(T)
    if n == 1:
        return T
    center = (n - 1) // 2
    left = sort(T[:center + 1])
    right = sort(T[center + 1:])
    return scal(left, right)

T = []
for counter in range(1000000):
    T.append(randint(1,1000000))


# lista = [randint(1,1000000) for _ in range(1000000)]

result = sort(T)

with open("wyniki_3.txt", "w") as file:
    for number in result:
        file.write(str(number) + "\n")