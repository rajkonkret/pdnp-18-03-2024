# instrukcja warunkowa
# uzależnia wykonanie programu od wyniku wyrażenia - bool
# instrukcje sterowania przepływem programu
# if - jezeli
# if warunek:
#     komenda_do_wykonaia - gdy warunek spełniony
# po : musi byc jedna komenda python umieszczona po wcieciu (4 spacje)

odp = True
# odp = False

if odp:
    print("Brawo")

print("Dalsza częśc programu")

if odp:  # gdy warunek True
    print("Brawo")  # obowiązkowo wcięcie
else:  # w przeciwnym przypadku
    print("Musisz się uczyc")  # # obowiązkowo wcięcie

print("Dalsza częśc programu")

if odp:
    pass  # nic nie rób

print("Dalej")

# podatek = 0.9  # 90%
# zarobki = int(input("podaj dochód"))  # zamieniamy na liczbę bo input zwraca stringa
# if zarobki < 10000:  # do 9999
#     podatek = 0.0
# elif zarobki < 30000:  # od 10000 do 29999
#     podatek = 0.2
# elif zarobki < 100000:  # od 30000 do 99999
#     podatek = 0.6
# else:  # od 100000
#     podatek = 0.9
# print(f"Zapłacisz {zarobki * podatek} pln")
# # dodac aby dla przedziału 10000 do 29999 podatek był 0.2 (20%)
# # kolejnośc ma znaczenie, po wykonaniu warunku spełnionego następne nie są juz sprawdzane

suma_zam = 150
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabacik {rabacik}")

rabat = 25 if suma_zam > 150 else 0
print(f"Rabacik {rabat}")

# zasymulejemy system analizy logów
# dane przyjdą w zmiennych
# na podstawie wartości tych zmiennych bedziemy wykonywac rózne działąnia
# console, email i inny
# error = -> critical, medium, inny
# w przypadku błedy w kocoli (alert_sysytem bedzie console) wyswietlamy komunika, ze nastąpił błąd
# w przydku systemu email do listy wpisywac bedziemy opisy poziomów błedó np.: critical -> krytyczny

alert_system = 'console'
error = 'critical'
error_list = []

if alert_system == "console":
    print("Stało się coś strasznego!!!")
elif alert_system == 'email':
    if error == 'critical':
        error_list.append('Krytyczny')
    elif error == 'medium':
        error_list.append('Ostrzeżenie')
    else:
        print("Inny bład, idź na kawę")
else:
    print("Nie znam takiego systemu")

# Stworzyc program - test z .....
# pobrac odpowiedz
# sprawdzic warunek

odp = input("Podaj nazwe stolicy Polski")
if odp.upper().replace(" ", "") == 'WARSZAWA':
    print("Prawidłowa odpowiedź")
else:
    print("Sprawdź w wikipedii")
# dodac kilka pytań i licznik prawidłowych odpowiedzi
