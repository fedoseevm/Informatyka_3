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


def IfASC(T):
    for i in range(len(T) - 1):
        if T[i] > T[i + 1]:
            return False
    return True


numbers = [int(input(f"Podaj {i + 1} liczbe ciagu: ")) for i in range(10)]

a = int(input("\nPodaj calkowita liczbe a: "))
if not IfASC(numbers):
    print("Ciag musi byc uporza dkowany niemalejaco")
else:
    if BinarySearchRecu(numbers, a, 0, len(numbers) - 1):
        print("tak")
    else:
        print("nie")
