numbers = []
with open("pi_przyklad.txt", "r") as file:
    for line in file:
        line = line.strip()
        numbers.append(line)
print(numbers)

n = len(numbers)
counter = 0
for i in range(0, n - 1, 2):
    pair = int(numbers[i] + numbers[i + 1])
    print(pair, end=" ")
    if pair > 90:
        counter += 1
print(counter)

