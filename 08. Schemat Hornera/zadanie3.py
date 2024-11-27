def HornerRecu(x, a):
    if len(a) == 1:
        return a[0]
    return x * HornerRecu(x, a[1:]) + a[0]

A = list(map(int, input("Podaj współczynniki wielomianu jako liczby rozdzielone spacjami: ").split()))
x = int(input("Podaj x: "))

print(f"Wartość wielomianu W({x}) = {HornerRecu(x, A)}")