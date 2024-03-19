try:
    # print(5 / 0)  # ZeroDivisionError: division by zero
    # print("a" / 2)
    print(int("A"))
    print(1 + 2)
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartości")
except Exception as e:  # Wszytskie błedy
    print("Bład", e)
else:
    print("Tylko gdy nie ma błedu")
finally:
    print("Wykona sie zawsze")

print("Działam dalej")
# TypeError, ValueError
# print("a" / 2)  # TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print(int("A"))  # ValueError: invalid literal for int() with base 10: 'A'
# try except [else, finally]
