# lista - kolekcja, przechowuje dowolną ilość danch dowolnego typu na raz
# zachowuje kolejnosć przy dodawaniu elementów

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

# append() - dodanie elemntu do listy
lista.append("Radek")
lista.append("Maciek")
lista.append("Szymon")
lista.append("Zenek")
lista.append("Paulina")
lista.append("Magda")
print(lista)  # ['Radek', 'Maciek', 'Szymon', 'Zenek', 'Paulina', 'Magda']
#                   0        1         2         3          4         5
#                   -6       -5        -4        -3         -2       -1
print(lista[0])  # wypisanie elementu z listy o indeksie 0
print(lista[2])
print(lista[3])
# print(lista[10])  # IndexError: list index out of range
print(len(lista))  # 6 elementów czyli indeks ostatni 5
print(lista[5])  # Magda
print(lista[-1])  # Magda
print(lista[-3])  # Zenek
# slicowanie listy (wyswietlanie czesci elementów)
print(lista[0:3])  # 0,1,2 ['Radek', 'Maciek', 'Szymon']
print(lista[:3])  # ['Radek', 'Maciek', 'Szymon']
print(lista[4:5])  # ['Paulina']
print(lista[10:12])  # []
print(lista[-2:0])  # []
print(lista[0:-2])  # ['Radek', 'Maciek', 'Szymon', 'Zenek']
print(lista[0:5:2])  # ['Radek', 'Szymon', 'Paulina']  start:stop:step(krok)
print(lista[0::2])  # ['Radek', 'Szymon', 'Paulina']
print(lista[::2])  # ['Radek', 'Szymon', 'Paulina']
print(lista[::-1])  # ['Magda', 'Paulina', 'Zenek', 'Szymon', 'Maciek', 'Radek'] - odwracanie listy

# nadpisanie elementu o indeksie 2 w liscie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek', 'Paulina', 'Magda']

# dodanie elementu we wskazanym miejscu
lista.insert(1, "Katarzyna")
print(lista)  # ['Radek', 'Katarzyna', 'Maciek', 'Mikołaj', 'Zenek', 'Paulina', 'Magda']

# usunięcie elementu z listy
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Katarzyna', 'Maciek', 'Zenek', 'Paulina', 'Magda']

lista.append("Zenek")
# print(lista.remove("Zenek")) None
lista.remove("Zenek")
print(lista)  # usunie pierwszego napotkanego

print("Zenek" in lista)  # True

# sprawdzenie indeksu elemnentu
indeks = lista.index("Maciek")
print(indeks)

# usunięcie elemntu po indeksie
print(lista.pop(indeks))  # Maciek - zwraca element usunięty
print(lista)  # ['Radek', 'Katarzyna', 'Paulina', 'Magda', 'Zenek']
print(lista.pop())  # usunie ostatni element z listy Zenek

a = 1
b = 3
a = b
print(a)  # 3
b = 7
print(a)  # 3

lista2 = lista  # kopiujemy referencje (adres pamieci)
lista3 = lista.copy()  # kopia elementow listy do nowej listy
lista.clear()  # czyszczenie elementów listy
print(lista2)
print(id(lista))  # 1596402618752
print(id(lista2))  # 1596402618752
print(lista3)
print(id(lista3))  # 1596402940032
