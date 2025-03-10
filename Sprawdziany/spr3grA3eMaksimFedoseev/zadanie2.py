def isASC(T):
    for i in range(len(T) - 1):
        if T[i] >= T[i + 1]:
            return False
    return True


with open("ciagi.txt", "r") as file:
    ciagi = file.readlines()
    for line in ciagi:
        ciag = list(map(int, line.split()))
        if isASC(ciag):
            print(ciag)