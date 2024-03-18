tekst = "Witaj świecie"
print(tekst)
print(type(tekst))
# teksty są niemutowalne
# """ Return a copy of the string converted to uppercase. """
tekst.upper()  # to zwraca nowy tekst z zamienionymi literami, ale nie zmienia oryginalnego tekstu
print(tekst)  # Witaj świecie
print(tekst.upper())
tekst_2 = tekst.upper()
print(tekst_2)
print(tekst)

tekst3 = tekst.lower()
print(tekst3)
print(tekst)

print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst)  # Witaj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'  - zapis binarny(b) \xc5 - wliczba w kodzie szesnastkowym
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 0123 -> Wita
# pierwszy element ma index 0
# 0, 4 - wez od indeksu zero włacznie do indeksy 4 (niewłącznie)
print(tekst.count("i", 5, 9))  # indeksy - 5678
print(tekst.count("j", 0, 4))  # 0
print(tekst)  # Witaj świecie

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b Dodatkowe zdanie"
print(tekst_format)  # f string - format string
# \t - tabulator
# \n - nowa linia
# \b - backspace - usuneło (.)
# Witaj świecie
# 	Mam na imię Radek
#  i lubię Pythona Dodatkowe zdanie

starszy = "Witaj %s!"  # %s - oczekuje stringa
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

# tekst wilolinijkowy
print("""
tekst
    wielolinijkowy
    tabulacja""")
# "tekst
#     wielolinijkowy
#     tabulacja"
