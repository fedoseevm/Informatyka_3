a, b = map(int, input("Podaj przedzial (a i b): ").split())

czy_pierwsza = [True] * (b - a + 1)
print(czy_pierwsza)
czy_pierwsza[0] = False
czy_pierwsza[1] = False

p = 2
while p * p < b:
    if czy_pierwsza[p]:
        for i in range(p * p, len(czy_pierwsza), p):
            czy_pierwsza[i] = False
    p += 1

for i in range(len(czy_pierwsza)):
    if czy_pierwsza[i]:
        print(i + a, end=" ")
