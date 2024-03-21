# REST API - sposób komunikacji i wymiany danych pomiędzy klientem a serwerem
# klient - przeglądarka  - front
# serwer - tzw backend, serwer który wystawia endpointy api i potrafi obsłużyc zapytania
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobiera dane
# POST - przesyłą dane do serwera - serwer np zapisze do bazy te dane - tworzy nowy zasób
# do przesylania danych może wykorzystać obiekty typu json
# PUT/PATCH - modyfikowanie elemntu na zasobie
# DELETE - usunięcie
# CRUD - Create, Read, Update, Delete
# przegladarka uzywa GET
import requests

url = 'http://api.open-notify.org/astros.json'

# GET
response = requests.get(url)
print(response)  # <Response [200]> ok

# 2xx - ok
# 3xx - przekierowania
# 4xx - bład po stronie klienta 404 - brak zasobu, 400 Bad Request - błedne rządanie
# 5xx błedy po stronie serwera
print(response.text)
response_data = response.json()
print(type(response_data))  # <class 'dict'>

# wypisac klucze ze słownika
# klucze i wartosci przypisane do nich
for k, v in response_data.items():
    print(k, "=>", v)
# message = > success
# people = > [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'}, {'name': 'Andreas Mogensen', 'craft': 'ISS'},
#             {'name': 'Satoshi Furukawa', 'craft': 'ISS'}, {'name': 'Konstantin Borisov', 'craft': 'ISS'},
#             {'name': 'Oleg Kononenko', 'craft': 'ISS'}, {'name': 'Nikolai Chub', 'craft': 'ISS'},
#             {'name': "Loral O'Hara", 'craft': 'ISS'}]
# number = > 7
print(response_data['people'])
# [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'}, {'name': 'Andreas Mogensen', 'craft': 'ISS'},
#  {'name': 'Satoshi Furukawa', 'craft': 'ISS'}, {'name': 'Konstantin Borisov', 'craft': 'ISS'},
#  {'name': 'Oleg Kononenko', 'craft': 'ISS'}, {'name': 'Nikolai Chub', 'craft': 'ISS'},
#  {'name': "Loral O'Hara", 'craft': 'ISS'}]
print(response_data['people'][0])  # {'name': 'Jasmin Moghbeli', 'craft': 'ISS'}
for i in response_data['people']:
    print(i['name'])
# Jasmin Moghbeli
# Andreas Mogensen
# Satoshi Furukawa
# Konstantin Borisov
# Oleg Kononenko
# Nikolai Chub
# Loral O'Hara
