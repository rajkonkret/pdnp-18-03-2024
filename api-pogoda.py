import requests as re

url = 'https://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid={API KEY}&lang=p&format=json&units=metric'

page = re.get(url)
print(page)
json = page.json()
print(json)
# {'coord': {'lon': 21.0118, 'lat': 52.2298},
#  'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations',
#  'main': {'temp': 8.08, 'feels_like': 6.15, 'temp_min': 6.47, 'temp_max': 9.75, 'pressure': 1014, 'humidity': 86},
#  'visibility': 7000, 'wind': {'speed': 3.09, 'deg': 270}, 'clouds': {'all': 75}, 'dt': 1711096407,
#  'sys': {'type': 2, 'id': 2035775, 'country': 'PL', 'sunrise': 1711081995, 'sunset': 1711126329}, 'timezone': 3600,
#  'id': 756135, 'name': 'Warsaw', 'cod': 200}
print(json['main']['temp'])
print(json['name'])
# 8.47
# Warsaw
