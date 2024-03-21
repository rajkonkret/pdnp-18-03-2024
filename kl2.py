class Human:
    """
    Klasa Human opisująca człowieka w python
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        # print(f"Nazywam się {self.imie}")
        return f"Nazywam się {self.imie}"  # f - fstring

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def ruszaj(self):
        if self.plec == "k":
            # print("Ruszyłam w drogę")
            return "Ruszyłam w drogę"
        else:
            # print("Ruszyłem w drogę")
            return "Ruszyłem w drogę"


cz1 = Human("Radek", 45, 190, "m")
print(cz1.imie)
print(cz1.wzrost)
cz1.powitanie()
cz1.wypisz_wzrost()

cz2 = Human("Zosia", 34, 170)
cz2.powitanie()
cz1.ruszaj()
cz2.ruszaj()
print(cz2.powitanie(), cz2.ruszaj())
# Nazywam się Zosia Ruszyłam w drogę
