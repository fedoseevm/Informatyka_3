with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readlines()))
print(numbers)

def quickSort(table):
    n = len(table)
    if n < 2:
        return table
    pivot = table[n // 2]
    left = [x for x in table if x < pivot]
    center = [x for x in table if x == pivot]
    right = [x for x in table if x > pivot]
    return quickSort(left) + center + quickSort(right)

quickSort(numbers)
print(quickSort(numbers))