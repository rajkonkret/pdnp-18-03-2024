# funkcja obliczająca średnią ocen
def liczby(name=None, *cyfry):  # * przyjmuje argumenty pozycyjne
    print(cyfry)
    suma = 0
    count = len(cyfry)
    suma2 = sum(cyfry)
    print(suma2)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Uczeń {name}, średnia wynosi", avg)
    finally:
        print("Koniec działania")


liczby()
liczby("Radek", 1, 2, 3, 4)
liczby("Tomek", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# liczby(a=1)  # TypeError: liczby() got an unexpected keyword argument 'a'
# print("radek", "Tomek", 'michal')
# # sep=' ', end='\n'
# # sep
# #         string inserted between values, default a space.
# #       end
# #         string appended after the last value, default a newline.
# print("radek", "Tomek", 'michal', sep=";")
# # radek;Tomek;michal
# print("linia jeden", end='')
# print("linia dwa")  # linia jedenlinia dwa
# print("linia 3")  # linia 3
# name, *cyfry = ("Radek", 1, 2, 3, 4)
