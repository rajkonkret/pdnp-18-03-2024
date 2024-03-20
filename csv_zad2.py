import csv

filename = 'records2.csv'
# filename = 'records.csv'

fields = []
rows = []

with open(filename, "r") as file:
    dialect = csv.Sniffer().sniff(
        file.read(1024))  # wyszukje w pliku csv jaki został użyty znak podziału, cudzysłow itd.
    print(dialect.delimiter, dialect.quotechar, dialect.escapechar)
    file.seek(0)  # ustawienie odczytu na początek pliku
    # csvreader = csv.reader(file, delimiter=";")
    csvreader = csv.reader(file, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x000001B3B22D10C0>

    fields = next(csvreader)  # bierzemy pierwszy element, wskaźnik ustawiany jest na następny czyli drugi element
    for row in csvreader:  # petla wystartuje od drugiego elementu bo next() przestawił wskaźnik na numer dwa
        # print(row)
        rows.append(row)

print(fields)
print("-----")
print(rows)
print(rows[1][0])  # marek
print(fields[0])  # name
