# json - {"name" : "Radek"}
# obiekt typu klucz wartość
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# tworzennie jsona ze słownika - serializacja
dict_json = json.dumps(person_dict)
print(dict_json)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(dict_json))  # <class 'str'>

# zapisanie słownika jako json do pliku
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)

# zapisanie w formacie ładniejszym
with open('nasze_dane.json', 'w') as file:
    json.dump(person_dict, file, indent=4)

# posortowac po kluczach
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>

print(data.keys())
print(data.values())
print(data.items())
print(data['name'])
print(data.get('name'))

print(dict_json)
print(type(dict_json))
data_dict = json.loads(dict_json)
print(data_dict)
print(type(data_dict))
# {"name": "Radek", "age": 40, "czy_pali": null}
# <class 'str'>
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
# <class 'dict'>