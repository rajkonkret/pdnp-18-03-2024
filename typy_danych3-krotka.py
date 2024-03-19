# krotka - niezmienna kolekcja
# jednoelementowa krotka jest jak zmienna ale stała

tupla = "radek"
print(type(tupla))  # str
tupla2 = ("Radek")
print(type(tupla2))  # str
tupla3 = "radek",
print(type(tupla3))  # <class 'tuple'>
tupla4 = ("radek",)  # PEP8 zaleca jednoelementowe tuple umieszczac w nawiasie
print(type(tupla4))  # <class 'tuple'>

temp = 36, 6
print(temp)  # (36, 6)
print(type(temp))  # <class 'tuple'>

tuple_names = "Radek", "Tomek", "Zenek", "Bartek"
tuple_names2 = ("Radek", "Tomek", "Zenek", "Bartek")
print(type(tuple_names))  # <class 'tuple'>
print(type(tuple_names2))  # <class 'tuple'>

# są immutable
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment
# del temp[0] - usunięcie elementu z krotki SyntaxError: cannot delete expression
del temp  # usunięcie całej krotki(tupli) z pamięci
# print(temp)  # NameError: name 'temp' is not defined

print(tuple_names[0])
print(tuple_names[1:3])
print(tuple_names[:3])
print(tuple_names[2:])
# Radek
# ('Tomek', 'Zenek')
# ('Radek', 'Tomek', 'Zenek')
# ('Zenek', 'Bartek')
print(tuple_names[-1])  # ostatni element Bartek
print(tuple_names[:])  # wypisanie całej tupli ('Radek', 'Tomek', 'Zenek', 'Bartek')

# sprawdzenie czy dany element istnieje w tupli
print("Radek" in tuple_names)  # True

print(tuple_names.count("Tomek"))  # 1 policzenie ile razy elemnt występuje
print(tuple_names.index("Tomek"))  # index 1 - indeks elementu

# sortowanie sorted()
print(sorted(tuple_names))  # sortowanie zwróci listę ['Bartek', 'Radek', 'Tomek', 'Zenek']
print(sorted(tuple_names, reverse=True))  # ['Zenek', 'Tomek', 'Radek', 'Bartek']

# rozpakowanie krotki
a, b = 1, 2
print(a, b)  # 1 2
print(type((1, 2)))  # <class 'tuple'>
print(a)
print(b)

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * - worek na pozostałe dane
print(a, b)  # 1 [2, 3]

*a, b = 1, 2, 3
print(a, b)  # [1, 2] 3
# tupla_names - wypisac w róznych warinatach rozpakowanie do trzech zmiennych imie1, imie2, imie3

imie1, imie2, *imie3 = tuple_names
print(imie1, imie2, imie3)
imie1, *imie2, imie3 = tuple_names
print(imie1, imie2, imie3)
*imie1, imie2, imie3 = tuple_names
print(imie1, imie2, imie3)
# Radek Tomek ['Zenek', 'Bartek']
# Radek ['Tomek', 'Zenek'] Bartek
# ['Radek', 'Tomek'] Zenek Bartek

lista = list(tuple_names)  # rzutowanie krotki na listę
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Bartek']
print(type(lista))  # <class 'list'>
print(len(tuple_names))  # długosc 4 elementy
