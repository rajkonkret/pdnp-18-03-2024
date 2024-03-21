# dziedziczenie
# mamy klasę opisująca obiekt
# podklasy, któe dziedziczą cechy z innej kalsy, dodają lub nadpisują swoje funkcjonalnosci i pola
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczenie po klasie Pojazd
    """
    Klasa samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)  # musimy wywołać kontruktor klasy z której dziedziczymy
        self.marka = marka

    def info(self):
        super().info()  # możemy wywołać metode z klasy po której dziedziczymy
        print(f"Marka: {self.marka}")


poj = Pojazd("czerwony")
poj.info()

sam = Samochod("zielony", "Opel")
sam.info()

lista = [poj, sam]
for i in lista:
    i.info()

# polimorfizm - obiekty róznych klas dziedziczace po wspolnej klasie posiadaja te same cechy i funkcje
# mozna wykonac takie same operacje na tych obiektach i traktowac je w zakresie tych funkcji jako obiekty wspólne