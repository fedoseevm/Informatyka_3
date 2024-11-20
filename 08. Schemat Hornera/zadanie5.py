def NaiveReversed(x, a):
    n = len(a) - 1
    result = a[n]
    power = 1
    for i in range(n - 1, -1, -1):
        power *= x
        result += a[i] * power
    return result

def HornerReversed(x, a):
    n = len(a) - 1
    result = A[0]
    for i in range(1, n + 1):
        result = x * result + A[i]
    return result


A = list(map(int, input("Podaj współczynniki wielomianu w kolejności od współczynnika przy najwyższej potędze do wyrazu wolnego jako liczby rozdzielone spacjami: ").split()))
x = int(input("Podaj x: "))
print(f"Wartość wielomianu W({x}) = {NaiveReversed(x, A)}")
print(f"Wartość wielomianu W({x}) = {HornerReversed(x, A)}")
