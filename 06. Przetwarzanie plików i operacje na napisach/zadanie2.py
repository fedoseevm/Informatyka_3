with open("dane_osobowe.txt", "r") as plik:
    dane_osobowe = list(plik.read().split())
print(f"Witaj {dane_osobowe[0]} {dane_osobowe[1]}")