with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readlines()))
print(numbers)

def quickSort(table):
    n = len(table)
    if n < 2:
        return table
    pivot = table[n // 2]
    left = []
    center = []
    right = []
    for x in table:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            center.append(x)
        elif x > pivot:
            right.append(x)
    return quickSort(left) + center + quickSort(right)

quickSort(numbers)
print(quickSort(numbers))