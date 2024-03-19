# napiac apliakcje kalkulator
# wykorzystac jako główną pętle programu pętlę while +
# umieścic klawisz ucieczki +
# pobrac od uzytkownika rodzaj operacji +
# pobrac liczby +
# wyswietlic wynik +
# obsłużyc wyjątki +
# praca domowa - przerobic na match case
while True:
    print(f"""
1. Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie
5. Koniec""")
    odp = input("Podaj opcje menu")
    if odp == '5':
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == '1':
            print(f"wynik odejmowania {a} + {b} = {a + b}")

        elif odp == "2":
            print(f"wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"wynik mnożenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"wynik dzielenia {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError as e:
        print("Nie dziel prez zero", e)
    except ValueError as e:
        print("Bład wartości", e)
    except TypeError as e:
        print("Bład typu", e)
    except Exception as e:
        print("Inny bład", e)
    else:
        print("Gdy nie ma błedu")
    finally:
        print("Zawsze")

while True:
    odp = input("Podaj wyrażenie")
    print(eval(odp))  # eval() - zwraca wynik podanego wyrażenia w stringu
