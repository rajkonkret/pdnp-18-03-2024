# baza danych - przechowywanie danych
# sql, nosql
import sqlite3  # baza danych w jednym pliku lub pamięci

try:
    conn = sqlite3.connect('baza_sqlite.db')  # połączenie z bazą danych
    c = conn.cursor()  # cursor - za pomoca kursora gadamy z bazą
    print("Baza danych została podłączona")

    query = '''
    CREATE TABLE IF NOT EXISTS sqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    with open('tables.sql', 'r') as f:
        sql_script = f.read()

    # c.execute(query)  # wykonanie polecenia na bazie danych
    # conn.commit()  # utrwalenie zmian - zacomitowanie
    c.executescript(sql_script)
    conn.commit()
except sqlite3.Error as e:
    print("Bład połaczenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
