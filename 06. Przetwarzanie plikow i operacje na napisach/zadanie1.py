imie, nazwisko = input("Podaj imie i nazwisko: ").split()

with open("dane_osobowe.txt", "w") as plik:
    plik.write(imie + "\n" + nazwisko)
