# petle
# for - petla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(1, 10):  # 1..9
    print(i)

my_string = "Radek"
for i in my_string:
    print(i)

# lotto
lista_wylosowane = []
lista_lotto = list(range(1, 50))
for i in range(6):
    wyn = random.choice(lista_lotto)
    lista_lotto.remove(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [11, 37, 6, 40, 5, 35]

for _ in range(4):  # niema zmienna
    print("Radek")
    print(_)
# 0
# Radek
# 1
# Radek
# 2
# Radek
# 3
for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

lista3 = [j for j in range(1, 10) if j % 2 == 0]
print(lista3)  # [2, 4, 6, 8]
for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print("Tylko wypisze 3", c)  # Tylko wypisze 3 3
    print("Wypisze wszystkie", c)  # Wypisze wszystkie 3

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)

# wyswietlic elemnty z listy wraz z indeksem
# 0 Radek
for p in imiona:
    print(imiona.index(p), p)

for i in range(len(imiona)):
    print(i, imiona[i])

# enumerate() - zwraca ponumerowane elementy
for p in enumerate(imiona):
    print(p)  # (3, 'Marcin')

for p, o in enumerate(imiona):
    print(p, o)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin
for p, o in enumerate(imiona, start=1):
    print(p, o)
# 1 Radek
# 2 Asia
# 3 Zbyszek
# 4 Marcin

# ludzie = ['Radek', 'Janek', 'Tomek', 'Marek']
# dla róznych długości listy dostaniemy bład w klasycznym podejściu
ludzie = ['Radek', 'Janek', 'Tomek', 'Marek', 'Magda']  # IndexError: list index out of range

wiek = [45, 56, 34, 32]
# Radek 45
# for x in range(len(ludzie)):
#     print(ludzie[x], wiek[x])
# Radek 45
# Janek 56
# Tomek 34
# Marek 32

# zip() - łączy kolekcje w jedną
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 45)
# ('Janek', 56)
# ('Tomek', 34)
# ('Marek', 32)
for p, w in zip(ludzie, wiek):
    print(p, w)
# Radek 45
# Janek 56
# Tomek 34
# Marek 32

zipped = zip_longest(ludzie, wiek, fillvalue=None)
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)  # rozpakowujemy elemnty z iteratora do listy aby móc wielokrotnie z nich skorzystać
for name, age in zipped_list:
    print(name, age)
# Radek 45
# # Janek 56
# # Tomek 34
# # Marek 32
# # Magda None
print("-----------")
for name, age in zipped_list:
    print(name, age)
# 0 Radek 45

for i in enumerate(zipped_list):
    print(i)  # (4, ('Magda', None))
a, b = (4, ('Magda', None))
print(a)
print(b)  # ('Magda', None)
c, d = ('Magda', None)
print(c, d)
print(a, c, d)  # 4 Magda None
for i, (p, w) in enumerate(zipped_list):
    print(i, p, w)
# 0 Radek 45
# 1 Janek 56
# 2 Tomek 34
# 3 Marek 32
# 4 Magda None

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # krok w tył
    print(i)

parzyste = [i for i in range(0, 10, 2)]
print(parzyste)
