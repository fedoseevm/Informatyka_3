with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readlines()))
print(numbers)

def quickSort(table, left, right):
    i = left
    j = right
    pivot = table[(i + j) // 2]
    while i <= j:
        while table[i] < pivot:
            i += 1
        while table[j] > pivot:
            j -= 1
        if i <= j:
            temp = table[i]
            table[i] = table[j]
            table[j] = temp
            i += 1
            j -= 1

    if j > left:
        quickSort(table, left, j)
    if i < right:
        quickSort(table, i, right)

quickSort(numbers, 0, len(numbers) - 1)
print(numbers)x