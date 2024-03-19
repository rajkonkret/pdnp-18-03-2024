# set - zbiór - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie na set set()
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # tworzenie pustego seta
print(zb2)  # pusty set wyswietla set()

# dodanie elemntów do zbioru
zb2.add(2)
zb2.add(2)
zb2.add(3)
zb2.add(3)
zb2.add(5)
print(zb2)  # {2, 3, 5}

print(zbior)
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

zb3 = set()
name = "Radek"
zb3.add(name)
print(zb3)  # {'Radek'}

# usunięcie elementu ze zbioru
zbior.remove(44)
print(zbior)  # {33, 66, 777, 11, 18, 22, 55}

# pop() - usuniecie pierwszego elemntu ze zbioru
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 18, 22, 55}
print(zbior.pop())  # 66
print(zbior)  # {777, 11, 18, 22, 55}
print(zbior.pop())  # 777

print(sorted(zbior))  # sortowanie zbioru zwraca liste [11, 18, 22, 55]

zbior2 = {667, 44, 18, 52, 55, 22, 687, 62, 999, 999}
print(zbior2)  # {999, 44, 687, 18, 52, 22, 55, 667, 62}
print(type(zbior2))  # <class 'set'>

zbior.add(17)
zbior2.add(17)

# zbiory można je porównywac
print(zbior | zbior2)  # suma zbiorów {999, 11, 44, 687, 17, 18, 52, 22, 55, 667, 62}
print(zbior.union(zbior2))  # {999, 11, 44, 687, 17, 18, 52, 22, 55, 667, 62}
# zbiory nie zostały zmodyfikowane
print(zbior)  # {11, 17, 18, 22, 55}
print(zbior2)  # {999, 44, 687, 17, 18, 52, 22, 55, 667, 62}

print(zbior & zbior2)  # czesc wspolna {17, 18, 22, 55}

print(zbior2 - zbior)  # {999, 44, 687, 52, 667, 62}
# {999, 44, 687, 17, 18, 52, 22, 55, 667, 62} - {11, 17, 18, 22, 55} = {999, 44,687, 52,62}
print(zbior2.difference(zbior))  # {999, 44, 687, 52, 667, 62}
print(zbior.difference(zbior2))  # {11}

zbior4 = zbior.copy()  # kopia elementów zbioru
print(zbior4)
zbior.clear()
print(zbior4)

print(zbior)  # set() - zbior pusty
print(zbior.union(zbior4))  # {17, 18, 22, 55, 11}
print(zbior)  # set() - nadal pusty - nie został zmieniony

zbior.update(zbior4)  # dodanie elemntów do zbioru - zmienia oryginalny zbior
print(zbior)  # zbior został zieniony {17, 18, 22, 55, 11}

print(len(zbior))  # 5

lista = list(zbior)  # rzutowania, zamiana zbioru nna liste
print(lista)  # [17, 18, 22, 55, 11]
