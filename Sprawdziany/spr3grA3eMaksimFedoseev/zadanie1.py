def horner(x, T, n):
    result = T[0]
    for i in range(1, n + 1):
        result = x * result + T[i]
    return result


with open("wielomian.txt","r") as file:
    n = int(file.readline())
    x = int(file.readline())
    wspolczynniki = list(map(int, file.readline().split()))

print(horner(x, wspolczynniki, n))