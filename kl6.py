# pracownik - imie, nazwisko, pensja
# menadżer - imie, nazwisko, pensja, premia
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} {self.nazwisko}.")

    def oblicz_pensja(self):
        return self.pensja


class Menadzer(Pracownik):

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensja(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 10000)
pracownik.przedstaw_sie()
wyna_prac = pracownik.oblicz_pensja()
print(f"Wynagordzenie: {wyna_prac}")  # Wynagordzenie: 10000

menago = Menadzer("Anna", "Nowak", 10000, 2000)
menago.przedstaw_sie()
wyna_m = menago.oblicz_pensja()
print(f"Wynagordzenie: {wyna_m}")  # Wynagordzenie: 10000
