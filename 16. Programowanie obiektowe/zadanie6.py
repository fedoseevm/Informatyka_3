class Trojkat:
    def __init__(self):
        self.a = int(input("Podaj a: "))
        self.b = int(input("Podaj b: "))
        self.c = int(input("Podaj c: "))
        self.wysokosc = 2 * (self.a + self.b + self.c) / self.a


trojkat1 = Trojkat()
print(trojkat1.wysokosc)