from random import randint


with open("losowe_w_linii.txt", "w") as file:
    for i in range(20): 
        file.write(str(randint(1, 10)))
        file.write(" ")
    file.write("\n")

frequency = [0] * 11
with open("losowe_w_linii.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

for number in numbers:
    frequency[number] += 1

print("Liczba występująca najczęściej:", frequency.index(max(frequency)))