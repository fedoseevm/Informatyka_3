def SumaDzielnikow(x):
    suma_dzielnikow = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            suma_dzielnikow += i
    return suma_dzielnikow

a, b = map(int, input("Podaj a i b: ").split())
if a != b and SumaDzielnikow(a) == b and SumaDzielnikow(b) == a:
    print("tak")
else:
    print("nie")
