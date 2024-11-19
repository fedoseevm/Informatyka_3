def Naive(x, a):
    result = a[0]
    power = 1
    for i in range(1, len(a)):
        power *= x
        result += a[i] * power
    return result

A = list(map(int, input("Podaj współczynniki wielomianu jako liczby rozdzielone spacjami: ").split()))
x = int(input("Podaj x: "))

print(f"Wartość wielomianu W({x}) = {Naive(x, A)}")