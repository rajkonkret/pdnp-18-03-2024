# wyjątki - błedy podczas wykonywania programu - powodują zatrzymanie programu
# try - except [else - finally]
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(5 / 0)
    raise ZeroDivisionError("Dzielenie przez zero")  # rzucenie wyjątku, wygenerowanie
except ZeroDivisionError as e:
    print("Nie dziel przez zero", e)

x = 0
try:
    if x == 0:
        raise MyException("X nie może byc 0")
except MyException as e:
    print("X nie moze byc 0", e)
# Nie dziel przez zero Dzielenie przez zero
# X nie moze byc 0 X nie może byc 0
