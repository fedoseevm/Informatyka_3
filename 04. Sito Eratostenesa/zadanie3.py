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


# czy_pierwsza[0] ← fałsz
# czy_pierwsza[1] ← fałsz
# dla i=2,3,...,n wykonuj
#   czy_pierwsza[i] ← prawda
# p ← 2
# dopóki p * p ⩽ n wykonuj
#   jeżeli czy_pierwsza[p]=prawda
#     index ← p * p
#     dopóki index ⩽ n wykonuj
#       czy_pierwsza[index] ← fałsz
#       index ← index + p
#   p ← p + 1
# dla i=2,3,...,n wykonuj
#   jeżeli czy_pierwsza[i]=prawda to
#     wypisz i
