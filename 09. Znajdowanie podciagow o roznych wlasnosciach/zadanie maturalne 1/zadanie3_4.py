# Wczytaj dane z pliku
with open("pi.txt", "r") as file:
    numbers = list(map(int, file.read().split()))
n = len(numbers)

result_position = 0
result_string = []

i = 0
while i < n - 1:
    # Przerwij, jeśli pozostałe elementy są krótsze niż aktualny najdłuższy wynik
    if n - i < len(result_string):
        break

    # Sprawdź, czy zaczyna się ciąg rosnący
    if numbers[i] < numbers[i + 1]:
        temp_position = i
        temp_string = []

        # Znajdź maksymalny ciąg rosnący
        while numbers[temp_position] < numbers[temp_position + 1]:
            temp_string.append(numbers[temp_position])
            temp_position += 1
        temp_string.append(numbers[temp_position])

        temp_position += 1

        # Znajdź maksymalny ciąg malejący
        while temp_position + 1 < n and numbers[temp_position] > numbers[temp_position + 1]:
            temp_string.append(numbers[temp_position])
            temp_position += 1
        temp_string.append(numbers[temp_position])

        # Aktualizuj wynik, jeśli znaleziono dłuższy ciąg
        if len(result_string) < len(temp_string):
            result_position = i + 1
            result_string = temp_string

        # Przeskocz do końca aktualnego ciągu
        i = temp_position - 1
    i += 1

print(result_position)
print(*result_string, sep="")
        