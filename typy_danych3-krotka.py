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
