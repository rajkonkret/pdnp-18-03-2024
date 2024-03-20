a = 10
b = 10


def dodaj():
    a = 6  # zmienne mają zasięg lokalny, nie wpływaja na wartośc globalnego a
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 8
    b = 9
    print(a + b)


print("Wartośc a z góry(globalne)", a)  # Wartośc a z góry(globalne) 10
dodaj()  # 13
print("Wartośc a z góry(globalne)", a)  # Wartośc a z góry(globalne) 10
dodaj2()  # 20
print("Wartośc a z góry(globalne)", a)  # Wartośc a z góry(globalne) 10
dodaj3()  # 17
print("Wartośc a z góry(globalne)", a)  # Wartośc a z góry(globalne) 8
dodaj2()  # 18
