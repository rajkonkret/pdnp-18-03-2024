import pickle

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mamy zapisac tą listę do pliku

with open('lista.txt', 'w') as f:
    f.write(str(lista))  # rzutownie na str

with open('lista.txt', 'r') as file:
    dane = file.read()

print(dane)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(dane))  # <class 'str'>
print(dane[0])  # [

print(dane.split())
print(dane.split(","))
# ['[1,', '2,', '3,', '4,', '5,', '6,', '7,', '8,', '9]']
# ['[1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9]']

with open('lista.pickle', "wb") as f:
    pickle.dump(lista, f)

with open('lista.pickle', "rb") as file:
    loaded_list = pickle.load(file)

print(loaded_list)
print(type(loaded_list))
print(loaded_list[0])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# <class 'list'>
# 1

# serializacja pickle - zamiana na postac bajtową
ser_lista = pickle.dumps(lista)
print(ser_lista)
# b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\te.'

# deerializacja - zamiana z postaci bajtowej na własciwą
print(pickle.loads(ser_lista))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
