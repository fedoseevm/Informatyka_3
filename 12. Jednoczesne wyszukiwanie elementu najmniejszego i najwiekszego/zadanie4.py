from random import randint

T = [randint(1,1000) for _ in range(99)]
n = len(T)
minimum = T[0]
maximum = T[0]
counter = 0

for i in range(1, n - 1, 2):
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
