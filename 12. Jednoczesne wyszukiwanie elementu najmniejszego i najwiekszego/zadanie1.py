from random import randint

T = [randint(1,1000) for _ in range(100)]

minimum = T[0]
maximum = T[0]
counter = 0
for i in range(1, len(T)):
    counter += 1
    if T[i] > maximum:
        maximum = T[i]
    counter += 1
    if T[i] < minimum:
        minimum = T[i]

print("Minimum: ", minimum)
print("Maximum: ", maximum)
print("Ilosc porownan: ", counter)