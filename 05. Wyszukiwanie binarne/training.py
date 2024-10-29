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

def BinarySearchRecu(T, a, left, right):
    if left > right:
        return False
    center = (left + right) // 2
    if T[center] == a:
        return True
    elif T[center] < a:
        return BinarySearchRecu(T, a, center + 1, right)
    else:
        return BinarySearchRecu(T, a, left, center - 1)
    
def BubbleSort(T):
    for i in range(len(T)):
        swapped = False
        for j in range(len(T) - i - 1):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
                swapped = True
        if not swapped:
            break
    return T

T = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(T)
print("Posortowana tablica: ", T)