with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readlines()))
print(numbers)

def quickSort(left, right):
    i = (left + right) // 2
    