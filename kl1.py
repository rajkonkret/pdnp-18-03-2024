# klasa - przepis, szablon
# pola
# funkcje
# obiekt - instancja klas, obiekt zbudowany na podstawie kalsy (szablonu)
# abstrakacja, hermetyzacja(enekapsulacja), dziedziczenie, polimorfizm

# deklaracja klasy - tu się nic nie wykonuje
class Human:
    """
    klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # metoda, która wypisze wiek dla danego obiektu


# tworzenie obiektu klasy Human
cz1 = Human()
print(type(cz1))  # <class '__main__.Human'>
print(cz1)  # <__main__.Human object at 0x000001FFF14C7AD0>
print(Human.__doc__)  # dokumentacja
#   klasa Human opisująca człowieka w pythonie
print(print.__doc__)
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)

cz1.wiek = 45
cz1.imie = "Anna"
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)

cz2 = Human()
cz2.plec = "m"
cz2.imie = "Radek"
cz2.wiek = 45

print(cz2.plec)
print(cz2.wiek)
print(cz2.imie)

cz2.powitanie()
cz1.powitanie()
# Nazywam się Radek
# Nazywam się Anna
