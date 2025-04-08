def wyrownajLiczby(number1, number2):
    if len(number1) > len(number2):
        maxLength = len(number1)
        number2 = '0' * (maxLength - len(number2)) + number2
    elif len(number1) < len(number2):
        maxLength = len(number2)
        number1 = '0' * (maxLength - len(number1)) + number1



p = int(input("Podaj podstawę systemu (2-9): "))
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")

result = ""


print(result)