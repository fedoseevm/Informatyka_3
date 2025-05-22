class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.a = dlugosc
        self.b = szerokosc

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return (self.a + self.b) * 2


prostokat1 = Prostokat(2,5)
print(f"Pole prostokąta o bokach {prostokat1.a} i {prostokat1.b} wynosi: {prostokat1.pole()}")
print(f"Obwód: {prostokat1.obwod()}")