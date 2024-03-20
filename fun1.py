# funkcje - wydzielony fragment kodu, można wykonac w dowolnej chwili, mozna wykonac wielokrotnie
# dekalracja funkcji musi być wcześniej niż użycie tej funkcji
a = 8
b = 9


# deklaracja funkcji - tu funkcja się nie wykonuje
def dodaj():  # funkcja bez argumentów
    print(a + b)


def dodaj2(a, b):  # funkcja ma dwa obowiązkowe argumenty
    print(a + b)  # a, b lokalne zmienne (zasięg lokalny)


# można zasymulować w pythonie przeciążanie argumentów funkcji
# poprzez argument o wartości domyślnej
def odejmij(a, b, c=0):
    print(a - b - c)


# uruchomienie funkcji (wywołanie)
dodaj()  # 17
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(6, 9)  # 15
odejmij(9, 5)  # 4
odejmij(9, 5, 2)  # 2 # przekazywanie argumentów po pozycji
odejmij(b=9, c=8, a=9)  # -8 argumenty przekazane po nazwie
odejmij(5, c=9, b=6)  # -10 sposób mieszany, argumenty pozycyjne na początku
print(dodaj())  # None
# print(dodaj() + dodaj2(9, 8))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
