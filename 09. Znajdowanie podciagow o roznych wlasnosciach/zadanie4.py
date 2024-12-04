with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
print(numbers)
n = len(numbers)

for startIndex in range(n - 3):
    for length in range(4, n - startIndex):
        print(*numbers[startIndex:startIndex + length])