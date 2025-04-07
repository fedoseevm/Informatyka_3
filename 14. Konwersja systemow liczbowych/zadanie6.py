binarna = input("Podaj liczbę binarną: ")

przecinek = binarna.index(',')
binarna = binarna[:przecinek] + binarna[przecinek + 1:]
stopien = przecinek - 1
result = 0

for cyfra in binarna:
    result += int(cyfra) * 2 ** stopien
    stopien -= 1
    
print(result)