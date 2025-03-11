from random import randint

T = [randint(1,1000) for _ in range(100)]
n = len(T)
if T[0] < T[1]:     # Perwsze porównanie
    minimum = T[0]
    maximum = T[1]
else:
    minimum = T[1]
    maximum = T[0]
counter = 1

for i in range(2, n, 2):
    counter += 1
    if T[i] < T[i + 1]:
        counter += 1
        if T[i] < minimum:
            minimum = T[i]
        counter += 1
        if T[i + 1] > maximum:
            maximum = T[i + 1]
    else:
        counter += 1
        if T[i + 1] < minimum:
            minimum = T[i + 1]
        counter += 1
        if T[i] > maximum:
            maksimum = T[i]

print("Minimum: ", minimum)
print("Maximum: ", maximum)
print("Ilosc porownan: ", counter)
