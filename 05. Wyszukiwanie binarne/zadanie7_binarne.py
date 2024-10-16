def BinarySearch(T, a, n):
    left = 0
    right = n - 1
    while left < right:
        center = (left + right) // 2
        if T[center] < a:
            left = center + 1
        else:
            right = center
    return T[left] == a


A = [0, 7, 99, 13, 73, 21, 111, 4, 180, 68, 24]
n = 10
# poczatek algorytmu
lewy = 1
prawy = n
while lewy < prawy:
    srodek = (lewy + prawy) // 2
    if A[srodek] % 2 == 1:
        lewy = srodek + 1
    else:
        prawy = srodek
w = A[lewy]
# koniec algorytmu
print(w)
