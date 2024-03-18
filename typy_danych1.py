import sys

wiek = 47
rok = 2024
temp = 36.6  # float
temp2 = 36, 6  # krotka

print(wiek)
print(type(wiek))
print(type(temp))
# <class 'int'>
# <class 'float'>

print(6 * "Radek")  # RadekRadekRadekRadekRadekRadek
print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # wynik float
# 2071
# -1977
# 95128
# 0.023221343873517788
print(wiek // rok)  # częśc całkowita dzielenia 0
print(wiek % rok)  # modulo - reszta z dzielenia
print(5 % 2)  # reszta 1bo 2 całe i reszta 1
# przy dzieleniu przez 2 reszta wynosi 0 lub 1 - 0 - parzyste, 1 - nieparzyste
print(wiek ** rok)  # potęgowanie
wyn = wiek ** rok
print(len(str(wyn)))  # str() - zamiana liczby na tekst, len() - długosc
# 3385

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.1 + 0.5)
print(0.1 + 0.2)  # 0.30000000000000004
print(0.2 + 0.7)  # 0.8999999999999999
# Liczy typu są narażone na bład zaokrąglenia
# x=SMB^{E}  - s - znak, m - mantysa, b - base, e - wykładnik
# w * 10^5
# w * 2^4
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")
print(f"""
{temp}
    {wiek}""")
