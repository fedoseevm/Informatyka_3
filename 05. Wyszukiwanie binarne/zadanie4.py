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
n = int(file.readline().rstrip())   # read first line
# print(n)
# lists = list(map(str, file.read().split("\n")))
for i in range(n):
    d = int(file.readline().rstrip())
    ciag = list(map(int, file.readline().split()))
    if BinarySearch(ciag, 10, d):
        print(ciag)
file.close()
