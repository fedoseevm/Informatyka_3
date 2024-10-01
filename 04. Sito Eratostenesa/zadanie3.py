n = int(input("Podaj n: "))
czy_pierwsza = [True] * (n + 1)
czy_pierwsza[0] = False
czy_pierwsza[1] = False

p = 2
while p * p <= n:
    if czy_pierwsza[p]:
        index = p * p
        while index <= n:
            czy_pierwsza[index] = False
            index += p
    p += 1

for i in range(2, n + 1):
    if czy_pierwsza[i]:
        print(i, end=" ")