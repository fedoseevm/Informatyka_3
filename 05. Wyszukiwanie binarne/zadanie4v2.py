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


file = open("ciagi2.txt", "r")
lines = file.readlines()
n = int(lines[0].rstrip())
file.close()

for i in range(n):
    d = int(lines[2 * i + 1].rstrip())
    ciag = list(map(int, lines[2 * i + 2].split()))
    if BinarySearch(ciag, 10, d):
        print(ciag)

