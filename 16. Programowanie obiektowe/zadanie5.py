class Osoba:
    def __init__(self):
        self.imie = input("Podaj imię: ")
        self.nazwisko = input("Podaj nazwisko: ")
        self.wzrost = int(input("Podaj swój wzrost: "))
        self.waga = int(input("Podaj swoją wagę: "))

    def powitanie(self):
        print(f"Witaj {self.imie} {self.nazwisko}")

    def informacje(self):
        print("Imię i nazwisko:", self.imie, self.nazwisko)
        print("Wzrost:", self.wzrost)
        print("Waga:", self.waga)


osoba1 = Osoba()
osoba1.powitanie()
osoba1.informacje()