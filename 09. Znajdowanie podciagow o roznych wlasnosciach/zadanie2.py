with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
print(numbers)
n = len(numbers)

for startIndex in range(n):
    for endIndex in range(startIndex + 1, n + 1):
        print(*numbers[startIndex:endIndex])
