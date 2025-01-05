with open("pi.txt", "r") as file:
    numbers = list(map(int, file.read().split()))
n = len(numbers)

result_position = 0
result_string = []

i = 0
while i < n - 1:
    if n - i < len(result_string):
        break
    if numbers[i] < numbers[i + 1]:
        temp_position = i
        temp_string = []

        while numbers[temp_position] < numbers[temp_position + 1]:
            temp_string.append(numbers[temp_position])
            temp_position += 1
        temp_string.append(numbers[temp_position])
        temp_position += 1
        while numbers[temp_position] > numbers[temp_position + 1]:
            temp_string.append(numbers[temp_position])
            temp_position += 1
        temp_string.append(numbers[temp_position])

        if len(result_string) < len(temp_string):
            result_position = i
            result_string = temp_string
        i = temp_position
    i += 1
print(result_position)
print(*result_string, sep="")
        