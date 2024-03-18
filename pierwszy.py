import sys

print()  # wypisz/wydrukuj
# dwa razy shift - podręczna wyszukiwarka
# Alt ctrl l - formatowanie kodu
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
# ctrl d - powielanie
print('Nazywam się Radek')
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-18-03-2024\pierwszy.py", line 12
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 12)
# ctrl / - komentarz zaznaczonych linii
print(type("Radek"))  # <class 'str'> tekst
print(39)  # sprawdzanie typu
print(type(39))  # <class 'int'> - liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)
print("59" + '14')  # 5914 - konkatenacja tekstów
print(39 + 56)
# print(39 + "56")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# nie zmienia typów sam
print(39 + int("56"))  # int() - rzutowanie na liczbę int - 95
print(str(39) + "56")  # teksty - konkatenacja - 3956  str() - rzutowanie na tekst
print(5 * "4")  # 44444

# zmienna - pudełko na dane (koszyczek)
# snake_case

name = 'Radek'
print(name)  # wypisanie zawartości zmiennej
print(type(name))  # <class 'str'>

name = 56
print(name)
print(type(name))  # <class 'int'>

name: str = 90  # str to tylko opis
print(name)  # 90
print(type(name))  # <class 'int'>

age = 48
print(age)
print(type(age))  # <class 'int'>
