# funkcja wewnętrzna, zagnieżdzona
# mechanizm funkcji wewnętrznej jest używany w dekoratorach
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres funkcji (referencje)


fun1()  # nazwa funkcji i nawiasy ()
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x00000220D5168CC0>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
