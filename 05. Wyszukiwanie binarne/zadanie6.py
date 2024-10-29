from random import randint


def BinarySearch(T, a, n):
    left = 0
    right = n - 1
    numberOfComparisons = 0
    while left < right:
        center = (left + right) // 2
        if T[center] == a:
            numberOfComparisons += 1
            return True, numberOfComparisons
        elif T[center] < a:
            left = center + 1
            numberOfComparisons += 1
        else:
            right = center
            numberOfComparisons += 1
    return T[left] == a, numberOfComparisons

lista = [randint(1, 10)]
for i in range(1, 1000000):
    lista.append(lista[i - 1] + randint(1, 3))

result = BinarySearch(lista, 1500000, len(lista)) # BinarySeach() zwraca 2 wartości w postaci tuple (boolean, int)
with open("zadanie4.txt", "w") as file:
    if result[0]:
        file.write(f"tak\n{result[1]}")
    else:
        file.write(f"nie\n{result[1]}")
