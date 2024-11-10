def scal(T1, T2):
    result = []
    n1 = len(T1)
    n2 = len(T2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if T1[i] < T2[j]:
            result.append(T1[i])
            i += 1
        else:
            result.append(T2[j])
            j += 1
    result.extend(T1[i:])
    result.extend(T2[j:])
    return result

def sort(T):
    n = len(T)
    if n == 1:
        return T
    center = (n - 1) // 2
    left = sort(T[:center + 1])
    right = sort(T[center + 1:])
    return scal(left, right)


with open("ciagi.txt", "r") as file:
    ciag1 = list(map(int, file.readline().split()))
    ciag2 = list(map(int, file.readline().split()))

ciag1.extend(ciag2)

result = sort(ciag1)
print(result)

with open("winiki_2.txt", "w") as file:
    for number in result:
        file.write(str(number) + " ")
