def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper  # adres funkcji


def bold_decorator(func):
    def wrapper():
        result = func()
        return "\033[1m" + result + "\033[0m"

    return wrapper

@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!"


print(greeting())  # HELLO WORLD!
print(greeting)  # <function uppercase_decorator.<locals>.wrapper at 0x000001EA20C5B420>
