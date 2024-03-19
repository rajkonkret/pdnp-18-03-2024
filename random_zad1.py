import random  # biblioteka do generowannia liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6
print(random.randrange(1, 6))  # int 1..5
print(random.randrange(6))  # int 0..5
print(random.random())  # float 0.6370941303594669 od 0 do 0.999999999
print(random.random() * 6)  # float 3.0477916031968437 od 0 do 5.999999

lista = [5, 7, 45, 34.56, 67]
print(random.choice(lista))  # 45

lista_lotto = list(range(1, 50))  # od 1 do 49
# print(lista_lotto)

wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)

print(random.choices(lista_lotto, k=6))  # losowanie z powtórzeniami [1, 30, 48, 48, 3, 39]
print(random.sample(lista_lotto, k=6))  # losowanie bez powtórzeń [9, 35, 11, 21, 7, 43]
print(random.sample(lista_lotto, 6))
