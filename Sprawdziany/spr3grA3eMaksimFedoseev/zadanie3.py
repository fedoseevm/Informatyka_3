with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))

n = len(numbers)
for i in range(n - 3):
    if sum(numbers[i:i + 4]) > 1:
        print(numbers[i:i + 4])