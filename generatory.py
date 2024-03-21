# genratory - funkcje zwracające kolejne wyniki
# nie przechowuje poprzednich wyników
# podstawia w kolejnosci
# efektywne zarządzenie pamięcią
# leniwe generowanie - dane dostarczone wtedy kiedy sa konieczne do zużycia
def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonuje operacje, zwraca wynik, zapamiętuje ostatni elemnt


kwa = kwadrat2(5)
next(kwa)
next(kwa)
next(kwa)
next(kwa)
print("Zrób cokolwiek")
lista = []
lista.append("1234")
print(lista)
print(next(kwa))


# print(next(kwa))  # StopIteration


def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


def counter_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


c2 = counter_down(10)
print(next(c2))
print(next(c2))
print(next(c2))
print(next(c2))

for i in counter_down(10):
    print(i)


def counter_2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c3 = counter_2(10)
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))
c3.send('Ok')
print(next(c3))
c3.send("q")  # StopIteration
# Process finished with exit code 1 - oznacza, że mamy błąd
