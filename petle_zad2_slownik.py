dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}
print(dictionary)
print(type(dictionary))

# wyswietli klucze
for k in dictionary:
    print(k)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wyswietlic same wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wyświetlenie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski

c = {'name': "Radek", 'age': 5}
print({v: k for k, v in c.items()})
# {'Radek': 'name', 5: 'age'}
d = {}
for k, v in c.items():
    d[v] = k

print(d)  # {'Radek': 'name', 5: 'age'}
