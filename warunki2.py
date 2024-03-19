# match case - od python 3.10
lista = []
# lang = input("Podaj znany Ci język programowania")
lang = [1, 2, 3]
# match lang.lower().replace(" ", ""):
match lang:
    case "python":
        print("Lubię pythona")
        lista.append(lang)
    case "java":
        print("java to kawa")
        lista.append(lang)
    case [a, b, c]:
        print(f"Lista z trzema elementami {a} {b} {c}")
    case _:  # wartość domyślna (else)
        print("Nie znam takiego języka")

print(lista)
# Lista z trzema elementami 1 2 3
