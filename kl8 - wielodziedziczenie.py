# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):  # dziedziczy po kalsie B i A
    """
    Klasa C dziedziczy po klasie B i A
    """


class D(A, B):
    """
    Kalsa dziedziczy po klasie A i B
    """

    def method(self):
        super().method()  # dzieedziczy po klasie nadrzędnej


class E(B, A):
    def method(self):
        print("Metoda z klasy E")  # nadpisujemy metodę


class G(A, B):
    def method(self):
        B.method(self)  # wskazanie by wykonało metode z klasy B


class H(A, B):
    def method(self):
        super().method()  # dziedziczy po A
        B.method(self)  # wyraźne wskazanie B
        print("Metoda z kalsy H")  # z klasy H


a = A()
a.method()
b = B()
b.method()
# Metoda z klasy A
# Metoda z klasy B
c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
d = D()
d.method()  # Metoda z klasy A
e = E()
e.method()  # Metoda z klasy E
g = G()
g.method()  # Metoda z klasy B
h = H()
h.method()
# Metoda z klasy A
# Metoda z klasy B
# Metoda z kalsy H
print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
