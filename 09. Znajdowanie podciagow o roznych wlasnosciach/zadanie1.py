with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
print(numbers)
n = len(numbers)

for length in range(1, n + 1):
    for startIndex in range(n - length + 1):
        print(*numbers[startIndex:startIndex + length], sep=", ")
# * usuwa nawiasy kwadratowe wyświetlanej listy
# parametr sep= pomaga określić znaki rozdzielające elementy wyświetlanej listy