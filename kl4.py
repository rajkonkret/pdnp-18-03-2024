# zrobic klase Dom +
# metraz, kolor, liczba_okien +
# pola maja byc prywatne +
# wystawic metody do odczytu i zapisu tych pól
# dodac metode prywatną farba() - ma wypisac: Zabrakło farby +
# wywoływac przy z mianie koloru
# dodać komentrze - dokumentacje
# uzyc tej klasy do zbudowania obiektu i wywolac metody

class Dom:
    """
    Klasa opsiująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        """
        Metoda inicjalizująca
        :param metraz:
        :param kolor:
        :param liczba_okien:
        """
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraz {self.__metraz} m2")

    def mam_okna(self):
        print(f"Mam {self.__liczba_okien} okna/okien")

    def __farba(self):
        print("Zabrakło farby")

    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")
        self.__kolor = odp
        self.mam_kolor()
        self.__farba()

    def zmien_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp
        self.mam_metraz()

    def zmien_okna(self):
        odp = int(input("Podaj nową liczbę okien"))
        self.__liczba_okien = odp
        self.mam_okna()


dom1 = Dom(200, "Biały", 12)
dom1.mam_metraz()
dom1.zmien_kolor()
dom1.zmien_metraz()
dom1.zmien_okna()
