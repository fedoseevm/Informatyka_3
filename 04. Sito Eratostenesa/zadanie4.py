czy_pierwsza = [True] * 1001
czy_pierwsza[0] = False
czy_pierwsza[1] = False

p = 2
print("Liczby pierwsze mniejsze lub rowne 1000: ")
while p * p < len(czy_pierwsza):
    if czy_pierwsza[p]:
        index = p * p
        while index < len(czy_pierwsza):
            czy_pierwsza[index] = False
            index += p
    p += 1

for i in range(2, len(czy_pierwsza)):
    if czy_pierwsza[i]:
        print(i, end=" ")



file = open("liczby.txt", "r")
liczby = list(map(int, file.read().split()))
file.close()

p = 2
ilosc = 0
for liczba in liczby:
    if czy_pierwsza[liczba]:
        ilosc += 1
print("\n\nIle liczb w pliku liczby.txt jest liczba pierwsza (1-10000): ", ilosc)
