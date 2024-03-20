# csv - dane oddzielone znakiem podziału ,;tab i podobne
import csv

# biblioteka do pracy z pilikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0.1']

dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0.1'}

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0.1'},
    {'name': 'marek', 'branch': 'cos', 'year': '2', 'cgpa': '8.1'},
    {'name': 'tomek', 'branch': 'cot', 'year': '1', 'cgpa': '6'},
    {'name': 'zenek', 'branch': 'coy', 'year': '7', 'cgpa': '67.4'},
]
print(dict_list[1]['year'])
filename = 'records.csv'

with open(filename, 'w') as csv_f:
    # zapis wiersz po wierszu
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records2.csv'
with open(filename, 'w', newline='') as f:
    # zapisanie do csv plików ze słownika
    csvwriter = csv.DictWriter(f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()  # zapisanie nagłówków
    # zapisanie pojedynczego słownika (eden wiersz)
    # csvwriter.writerow(dictionary)
    # zapisanie wielu wierszy z listy słowników
    csvwriter.writerows(dict_list)
# newline='' - ominięcie pustych linii
# delimiter= - znak podziału
