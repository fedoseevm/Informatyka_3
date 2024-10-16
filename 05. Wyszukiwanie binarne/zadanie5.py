def BinarySearch(T, a, n):
    left = 1
    right = n
    while left < right:
        center = (left + right) // 2
        if T[center] < a:
            left = center + 1
        else:
            right = center
    return T[left] == a

def IfASC(T):
    for i in range(1, len(T) - 1):
        if T[i] > T[i + 1]:
            return False
    return True

# numbers = list(map(int, input("Podaj ciag 10 uporzadkowanych niemalejaco liczb calkowitych: ").split()))
numbers = [int(input(f"Podaj {i + 1} liczbe ciagu: ")) for i in range(10)]
numbers.insert(0, 0) # Wstawianie 0 na początku listy numbers, aby pierwsza podana liczba na liscie miala index = 1

a = int(input("\nPodaj calkowita liczbe a: "))
if not IfASC(numbers):
    print("Ciag musi byc uporza dkowany niemalejaco")
else:
    if BinarySearch(numbers, a, len(numbers)):
        print("tak")
    else:
        print("nie")