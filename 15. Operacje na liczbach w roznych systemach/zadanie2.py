bin1 = input("Podaj pierwszą liczbę binarną: ")
bin2 = input("Podaj drugą liczbę binarną: ")

maxLength = max(len(bin1), len(bin2))
bin1 = bin1.zfill(maxLength)
bin2 = bin2.zfill(maxLength)

result = ""
przeniesienie = 0

for i in range(maxLength - 1, -1, -1):
    suma = int(bin1[i]) + int(bin2[i]) + przeniesienie
    result = str(suma % 2) + result
    przeniesienie = suma // 2

if przeniesienie:
    result = str(przeniesienie) + result

print(result)
