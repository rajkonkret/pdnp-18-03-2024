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
