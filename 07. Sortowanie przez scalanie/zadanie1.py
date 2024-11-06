def Scale(T, left, center, right):
    i = left
    j = center + 1
    k = left
    while i <= center and j <= right:
        if T[i] < T[j]:
            tempTable[k] = T[i]
            i += 1
        else:
            tempTable[k] = T[j]
            j += 1
        k += 1
    while i <= center:
        tempTable[k] = T[i]
        i += 1
        k += 1
    while j <= right:
        tempTable[k] = T[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        T[i] = tempTable[i]


def Sort(T, left, right):
    if left < right:
        center = (left + right) // 2
        Sort(T, left, center)
        Sort(T, center + 1, right)
        Scale(T, left, center, right)


ciag = list(map(int, input("Podaj ciag liczb: ").split()))
print(ciag)
tempTable = [0] * len(ciag)
Sort(ciag, 0, len(ciag) - 1)
print(ciag)