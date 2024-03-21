import requests

url = 'https://restcountries.com/v3.1/name/Poland'
response = requests.get(url)
print(response)
print(response.text)
# odczytac name -> common , official
# capital
# population
data = response.json()
print(type(data))  # <class 'list'>
country = data[0]  # pierwszy element z listy
print(f"Nazwa kraju: {country['name']}")
# Nazwa
# kraju: {'common': 'Poland', 'official': 'Republic of Poland',
#         'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
print(f"Nazwa główna: {country['name']['common']}")  # Nazwa główna: Poland
print(f"Nazwa oficjalna: {country['name']['official']}")  # Nazwa oficjalna: Republic of Poland
print(f"Stolica kraju: {country['capital']}")  # Stolica kraju: ['Warsaw']
print(f"Stolica kraju: {country['capital'][0]}")  # Stolica kraju: Warsaw

print(f"Liczba luności: {country['population']}")  # Liczba luności: 37950802
