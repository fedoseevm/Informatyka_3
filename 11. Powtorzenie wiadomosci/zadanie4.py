with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))

maxLen = 0
currentLen = 1
for i in range(len(numbers) - 1):
    if numbers[i] <= numbers[i + 1]:
        currentLen += 1
    else:
        if maxLen < currentLen:
            maxLen = currentLen
            currentLen = 0

print(maxLen)