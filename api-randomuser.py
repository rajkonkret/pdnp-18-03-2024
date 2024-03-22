import requests as re

url = 'https://randomuser.me/api/'
response = re.get(url)
print(response.text)
data_resp = response.json()
user = data_resp['results'][0]
print(user)
# {'gender': 'female',
# 'name': {'title': 'Ms', 'first': 'Pamela', 'last': 'Melgar'},
#  'location': {'street': {'number': 753, 'name': 'Privada Italia'},
#  'city': 'Puerto Escondido',
#  'state': 'Quintana Roo',
#   'country': 'Mexico', 'postcode': 89192, 'coordinates': {'latitude': '25.4828', 'longitude': '85.5396'},
#               'timezone': {'offset': '+4:30', 'description': 'Kabul'}}, 'email': 'pamela.melgar@example.com',
#  'login': {'uuid': 'd8ba1d9b-e99c-47f4-8467-451f6ec98244', 'username': 'heavyelephant400', 'password': 'goodtime',
#            'salt': 'MLVC7qbq', 'md5': '81099a44c6da441462d9ac37eb108b3c',
#            'sha1': 'f2e09c3bab38c3d903eed8870e4dfbf14afaf40b',
#            'sha256': '08ba48f8c393664058e4c0085faef682735646ad1c4425944561097773398ccc'},
#  'dob': {'date': '1949-01-01T09:22:14.459Z', 'age': 75}, 'registered': {'date': '2022-03-13T09:09:05.962Z', 'age': 2},
#  'phone': '(697) 551 3257', 'cell': '(617) 737 9766', 'id': {'name': 'NSS', 'value': '71 25 93 7347 0'},
#  'picture': {'large': 'https://randomuser.me/api/portraits/women/37.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/women/37.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/37.jpg'}, 'nat': 'MX'}
print(f"Imię: {user['name']}")  # Imię: {'title': 'Mrs', 'first': 'Slavina', 'last': 'Vatamanyuk'}
print(f"Imię: {user['name']['first']}")  # Imię: Rubén
print(f"Nazwisko: {user['name']['last']}")  # Nazwisko: Madsen
photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")  # Link do zdjęcia: https://randomuser.me/api/portraits/women/68.jpg

response_photo = re.get(photo_url)
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)  # content zawiera dane zdjęcia

print("Zdjęcie zostało zapisane")
