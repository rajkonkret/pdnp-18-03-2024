# słownik - para klucz:wartosc
# {'name' : 'Radek'} - para klucz wartosc
# odpowiednik jsona
# klucze nie mogą się powtarzać

my_dict = {"A": 'one', 'B': 'two', 'C': "three"}
print(type(my_dict))  # <class 'dict'> typ słownik
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three'}

# tworzenie pustego słownika
empty_dict = {}
empty_dict2 = dict()
print(empty_dict)  # {} - puste klamerki to słownik
print(empty_dict2)  # {}

dict_mixed = {1: 'one', 'A': 'two', 3: 'three'}
print(dict_mixed)  # {1: 'one', 'A': 'two', 3: 'three'}

print(dict_mixed.keys())
print(dict_mixed.values())
print(dict_mixed.items())
# dict_keys([1, 'A', 3])
# dict_values(['one', 'two', 'three'])
# dict_items([(1, 'one'), ('A', 'two'), (3, 'three')])

# dodane wielu elementów do słownika za pomocą tupli
dictionary = {'x': 2}
dictionary.update([('y', 2), ('z', 3)])
print(dictionary)  # {'x': 2, 'y': 2, 'z': 3}

# dodanie do słownika jedego elemntu
empty_dict['imie'] = "Radek"
print(empty_dict)  # {'imie': 'Radek'}
empty_dict['wiek'] = 39
print(empty_dict)  # {'imie': 'Radek', 'wiek': 39}

# nadpisanie wartości klucza
empty_dict['wiek'] = 43
print(empty_dict)  # {'imie': 'Radek', 'wiek': 43}

# wypisanie wartosci ze słownika dla danego klucza
print(empty_dict['wiek'])  # 43
print(empty_dict.get('wiek'))  # 43
print(empty_dict.get('wiek2', 'default'))
# print(empty_dict['wiek2'])  # KeyError: 'wiek2'

print(empty_dict.pop('wiek'))  # usunięcie klucza ze słownika
print(empty_dict)  # {'imie': 'Radek'}
empty_dict['age'] = 45
print(empty_dict)  # {'imie': 'Radek', 'age': 45}
print(empty_dict.popitem())  # usunie ostatni element i zwróci w postaci krotki ('age', 45)

empty_dict.clear()  # usunięcie danych ze słownika
print(empty_dict)  # {}

my_dict = dictionary.copy()  # kopiowanie elemntów
print(my_dict)  # {'x': 2, 'y': 2, 'z': 3}
odp = input("Podaj liczbę")  # input zwraca stringa
print(odp)
print(type(odp))  # <class 'str'>

# input zawsze zwraca stringa, musimy zamienic na liczby int() lub float()
a = input("podaj pierwszą liczbę")
b = input("podaj druga liczbę")
c = float(input("podaj liczbę c: "))
print(a + b)  # 12  - konkatenacja - łaczenie tekstów - kalkulator dziala źle bo na tekstach a nie liczbach
print(int(a) + float(b))  # 3.0 zamieniamy na liczby by wynik był liczbą
print("Liczba c:", c)  # Liczba c: 22.0

# Napisać program słownik
# pobrac słowo od uzytkownika
# wypisac polskie tłumaczenie tego słowa
dict_words = {'name': 'imie', 'castle': 'zamek', 'water': 'woda'}
print("Słowka dostępne", dict_words.keys())
odp = input("Podaj słowko do przetłumaczenia")  # str()
print(dict_words[odp.lower().replace(" ", "")])
