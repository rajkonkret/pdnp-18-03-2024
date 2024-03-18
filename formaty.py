user = "Tomek"  # str
wiek = 39  # int
wersja = 3.9000001  # float - zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 123456789123  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s masz teraz %d lat" % (user, wiek))
# sprawdza typy w tym przypadku
# print("Witaj %s masz teraz %d lat" % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, 'age': wiek})
# Witaj Tomek masz teraz 39 lat
# Witaj Tomek, masz teraz 39 lat
# Witaj Tomek, masz teraz 39 lat

# Process finished with exit code 0 - program zakonczony bez błedu
print(f"Witaj {user} maz teraz {wiek} lat.")
print("Witaj {} maz teraz {} lat.".format(user, wiek))
# Witaj Tomek maz teraz 39 lat.
# Witaj Tomek maz teraz 39 lat.

print("Uzywamy wersji pythona %i" % 3)
print("Uzywamy wersji pythona %f" % 3.8)  # Uzywamy wersji pythona 3.800000
print("Uzywamy wersji pythona %.1f" % 3.8)  # Uzywamy wersji pythona 3.8
print("Uzywamy wersji pythona %.2f" % 3.8)  # Uzywamy wersji pythona 3.80
print("Uzywamy wersji pythona %.0f" % 3.8)  # 4  - zaokrągla przy wyswietlaniu, nie zmienia wartosci zmiennej
print("Uzywamy wersji pythona %.f" % 3.8)  # Uzywamy wersji pythona 4

print(f"Używamy wersji Python: {wersja}")
print(f"Używamy wersji Python: {wersja:.1f}")
print(f"Używamy wersji Python: {wersja:.2f}")
print(f"Używamy wersji Python: {wersja:.0f}")
# Używamy wersji Python: 3.9000001
# Używamy wersji Python: 3.9
# Używamy wersji Python: 3.90
# Używamy wersji Python: 4
print(wersja)  # 3.9000001

print(f"{user:>20}")  # "               Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 123456789123
print("Nasza duża licznba {:,}".format(liczba))
# Nasza duża licznba 123,456,789,123
# zamienic przecinek na spacje lub kropkę
print("Nasza duża licznba {:,}".format(liczba).replace(",", " "))
print("Nasza duża licznba {:,}".format(liczba).replace(",", "."))
print(f"Nasza duża licznba {liczba:,}".replace(",", "."))
# Nasza duża licznba 123.456.789.123
