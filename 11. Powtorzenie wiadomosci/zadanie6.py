with open("ciag.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))

n = len(numbers)
maks = numbers[0]

for start in range(n):
    for length in range(1, n - start + 1):
        print(numbers[start:start + length])
        suma = sum(numbers[start:start + length])
        if maks < suma:
            maks = suma

print(maks)
