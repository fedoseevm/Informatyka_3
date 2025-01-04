with open("pi.txt", "r") as file:
    numbers = list(file.read().split())
n = len(numbers)
freq = {}   # Dictionary which contains key value pairs
for i in range(10):
    for j in range(10):
        freq[f"{i}{j}"] = 0

for i in range(n - 1):
    fragment = numbers[i] + numbers[i + 1]
    freq[fragment] += 1
print(freq)
minimum = min(freq.values())
maximum = max(freq.values())
for fragment in freq:
    if freq[fragment] == minimum:
        print(fragment, minimum)
        break
for fragment in freq:
    if freq[fragment] == maximum:
        print(fragment, maximum)
        break