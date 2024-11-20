def Horner(x, a):
    n = len(a)
    y = a[n]


A = list(map(int, input("Podaj współczynniki wielomianu jako liczby rozdzielone spacjami: ").split()))
x = int(input("Podaj x: "))

print(f"Wartość wielomianu W({x}) = {Horner(x, A)}")