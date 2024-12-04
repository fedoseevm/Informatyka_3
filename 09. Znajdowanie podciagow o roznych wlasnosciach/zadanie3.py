with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
print(numbers)
n = len(numbers)

for startIndex in range(n - 4):
    sum = 0
    subString = numbers[startIndex:startIndex + 5]
    for number in subString:
        sum += number
    print(sum)
    print(subString)
