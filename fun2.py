# funkcje zwracające wynik
def dodaj(a, b):
    return a + b  # return - zwróć wynik


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(7, 8))  # 15
wyn = dodaj(9, 15)
print(wyn)  # 24
print(odejmij())
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(b=8, c=9))
# print(odejmij(1, 2, 3, 4))  # TypeError: odejmij() takes from 0 to 3 positional arguments but 4 were given

print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=1000))

print(dodaj(8, 9) * oblicz_vat(1000))  # 20910.0
zm = oblicz_vat(1000)
print(zm)  # 1230.0
if zm == 1230:
    print("Ok")  # Ok
