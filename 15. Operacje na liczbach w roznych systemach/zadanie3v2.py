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
carry = 0

wyrownajLiczby(a, b)

for i in range(len(a) - 1, -1, -1):
    suma = int(a[i]) + int(b[i]) + carry
    result = str(suma % p) + result
    carry = suma // p

if carry:
    result = str(carry) + result

print(result)