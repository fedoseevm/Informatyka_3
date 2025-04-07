def toDec(string, base):
    result = 0
    power = 0
    for cyfra in reversed(string):
        result += int(cyfra) * base ** power
        power += 1
    return result
    
def fromDec(number, base):
    result = ""
    while number > 0:
        result = str(number % base) + result
        number //= base
    return result


p = int(input("Podaj podstawę systemu (2-9): "))
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")

decA = toDec(a, p)
decB = toDec(b, p)

suma = decA + decB

result = fromDec(suma, p)
print(result)