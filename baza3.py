# baza danych - przechowywanie danych
# sql, nosql
# CRUD - insert, select, update, delete
import sqlite3  # baza danych w jednym pliku lub pamięci

try:
    conn = sqlite3.connect('baza_sqlite.db')  # połączenie z bazą danych
    c = conn.cursor()  # cursor - za pomoca kursora gadamy z bazą
    print("Baza danych została podłączona")

    insert = """
    INSERT INTO software (id,name,price) VALUES (1,'Python', 200);
    """

    select = """
    SELECT * FROM software;
    """
    # c.execute(insert)
    # conn.commit()

    update = """
    UPDATE software SET price=1000 WHERE id=1;
    """
    for row in c.execute(select):
        print(row)  # (1, 'Python', 200.0)

    # c.execute(update)
    # conn.commit()

    delete = """
    DELETE FROM software WHERE id=1;
    """

    c.execute(delete)
    conn.commit()
except sqlite3.Error as e:
    print("Bład połaczenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
