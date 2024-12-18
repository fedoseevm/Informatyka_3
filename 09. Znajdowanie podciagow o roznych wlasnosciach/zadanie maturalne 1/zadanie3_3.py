def czy_rosnacy(x):
    for i in range(len(x) - 1):
        if x[i] >= x[i + 1]:
            return False
    return True


def czy_malejacy(x):
    for i in range(len(x) - 1):
        if x[i] <= x[i + 1]:
            return False
    return True


def czy_rosnaco_malejacy(ciag):
    for k in range(1, 4):
        if czy_rosnacy(ciag[:k + 1]) and czy_malejacy(ciag[k + 1:]):
            return True
    return False


with open("pi.txt", "r") as file:
    numbers = list(map(int, file.read().split()))
n = len(numbers)
counter = 0
for i in range(n - 5):
    if czy_rosnaco_malejacy(numbers[i:i + 6]):
        print(numbers[i:i + 6])
        counter += 1
print(counter)