# while - sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("komunikat!!!")
    if licznik > 10:
        break  # przerywa działąnie pętli

print(licznik)  # 11
licznik = 0
while licznik < 10:
    licznik += 1
    print("komunikat2!!!")

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)
print(lista2)
# ['1', '3', '67', '54', '23']
# [1, 3, 67, 54, 23]
