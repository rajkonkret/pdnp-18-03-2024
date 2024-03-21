from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, 'Ja nie latam.')

    def wydaj_odglos(self):
        print("Ko o ko ko")


class Orzel(Ptak):
    """
    Klasa orzel
    """

    def wydaj_odglos(self):
        print("Kier kieeer kir")


# ni ezadziała bo nie implementuje metody wydaj_odglos
# class Sowa(Ptak):
#     """
#     Klasa Sowa
#     """


# Po oznaczeniu klasy/metody jako abstarkcyjna nie mozna tworzyc obiektów tej klasy
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel", 40)
# or1.latam()  # Tu Orzel Lecę z szybkością 40
# or1.wydaj_odglos()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()
kur2.wydaj_odglos()

or2 = Orzel("Orzel", 45)
or2.latam()
or2.wydaj_odglos()
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sow = Sowa("Sowa", 15)
