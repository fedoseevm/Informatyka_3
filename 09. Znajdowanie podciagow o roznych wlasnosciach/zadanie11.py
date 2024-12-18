with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
    # numbers = [1, 2, 3, 4, 4, 0, 1, 2, 3, 0, 1, 2, 0]
print(numbers)
n = len(numbers)

max_length = 0
counter = 1
for i in range(n - 1):
    if numbers[i] <= numbers[i + 1]:
        counter += 1
    else:
        if max_length < counter:
            max_length = counter
        counter = 1
print(max_length)
