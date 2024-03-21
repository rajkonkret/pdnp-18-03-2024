class Car:
    """
    Klasa opisująca samochód w Pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # __predkosc - pole prywatne
        self.__predkosc = 0  # zawsze bedzie 0, nie chcemy przyjmować wartosci startowej z zewnątrz

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmien bieg")


car1 = Car("Multipla", 2024)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po oznaczeniu pola jako prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()
car1.__predkosc = 0  # Dodanie pola o nazwie __predkosc jako pola globalnego
car1.licznik()
print(car1.__predkosc)  # 0
