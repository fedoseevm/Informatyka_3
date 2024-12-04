with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
print(numbers)
n = len(numbers)

for startIndex in range(n):
    for endIndex in range(startIndex, n):
        print(*numbers[startIndex:endIndex + 1])
