with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
    # numbers = [1, 2, 3, 0, 4, 4, 5, 0, 6, 7, 0]
print(numbers)
numbers.append(0)
n = len(numbers)

# max_length = 0
# counter = 1
# resultString = []
# tempstring = []
# for i in range(n - 1):
#     if numbers[i] <= numbers[i + 1]:
#         counter += 1
#         tempstring.append(numbers[i])
#         # print(tempstring)
#     else:
#         tempstring.append(numbers[i])
#         if max_length < counter:
#             resultString = tempstring.copy()
#             print(tempstring)
#         counter = 1
#         tempstring.clear()
# print("Result: ", resultString)

max_length = 0
counter = 1
startIndex = 0
maxStartIndex = 0
for i in range(1, n):
    if numbers[i] >= numbers[i - 1]:
        counter += 1
    else:
        if max_length < counter:
            max_length = counter
            maxStartIndex = startIndex
        counter = 1
        startIndex = i
print(numbers[maxStartIndex:maxStartIndex + max_length])

