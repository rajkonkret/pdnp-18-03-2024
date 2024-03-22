# baza danych - przechowywanie danych
# sql, nosql
import sqlite3  # baza danych w jednym pliku lub pamięci

try:
    conn = sqlite3.connect('baza_sqlite.db')  # połączenie z bazą danych
    c = conn.cursor()  # cursor - za pomoca kursora gadamy z bazą
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Bład połaczenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
