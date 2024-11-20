def Horner(x, a):
    n = len(a) - 1
    result = a[n]
    for i in range(n - 1, -1, -1):
        result = x * result + a[i]
    return result


A = list(map(int, input("Podaj współczynniki wielomianu jako liczby rozdzielone spacjami: ").split()))
x = int(input("Podaj x: "))

print(f"Wartość wielomianu W({x}) = {Horner(x, A)}")
