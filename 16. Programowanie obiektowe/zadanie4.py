class Prostokat:
    a = int(input("Podaj dlugosc boku a: "))
    b = int(input("Podaj dlugosc boku b: "))

    def pole(self):
        return self.a * self.b


prostokat3 = Prostokat()
print("Pole prostokąta wynosi:", prostokat3.pole())