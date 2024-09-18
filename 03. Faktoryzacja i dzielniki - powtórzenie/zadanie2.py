plik = open('liczby2.txt', 'r')
numbers = list(map(int, plik.read().split()))
plik.close()

print(numbers)

for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        print(numbers[i])