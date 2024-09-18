import math


def IfPrime(x):
    for i in range(2, round(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


# with open('liczby1.txt', 'r') as file:
#     content = file.read()
# numbers = content.split()
# numbers = [int(num) for num in numbers]

plik = open('liczby1.txt', 'r')
numbers = list(map(int, plik.read().split()))
plik.close()

print(numbers)

ilosc = 0
for i in range(len(numbers)):
    if IfPrime(numbers[i]):
        ilosc += 1

print(ilosc)