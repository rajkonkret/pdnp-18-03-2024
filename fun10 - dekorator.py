# dekoratory
# działają na zasasdzie funkcji zagnieżdzonej
# dekorator przyjmuje funkcję jako argument i dodaje do niej nowe funkcje
def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # zwracamy wynik funkcji a nie adres

    return wew  # zwracamy adres funkcji wewnętrznej


@dekor
def hej():
    print("Hej")


@dekor
def dodaj():
    print(1 + 2)


hej()
dodaj()
