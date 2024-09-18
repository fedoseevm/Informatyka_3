plik = open('liczby2.txt', 'r')
numbers = list(map(int, plik.read().split()))
plik.close()

print(numbers)

ilosc_dzielnikow_wlasciwych = 0
for i in range(len(numbers)):
    for j in range(1, numbers[i] //2 + 1):
        if numbers[i] % j == 0:
            ilosc_dzielnikow_wlasciwych += 1
print(ilosc_dzielnikow_wlasciwych)