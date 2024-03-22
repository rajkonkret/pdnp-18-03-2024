import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

# utworzenie katalogu
base_path.mkdir()

path_b = base_path / 'A' / 'B'
# mkdir() tworzy tylko bieżacy katalog
# path_b.mkdir() # FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\B'
path_b.mkdir(parents=True)  # parents=True ma stworzyć całe drzewo katalogów
path_c = base_path / 'A' / 'C'
path_c.mkdir()  # zadziałą bo katalog A juz istnieje

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w', encoding='utf-8') as stream:
        stream.write(f"Jakaś treść pliku {filename}")

path_d = base_path / 'A' / 'D'
# przeniesienie plików/katalogó w nowe miejsce. usunie poprzednie
shutil.move(path_b, path_d)

# zmina nazwy pliku
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1renamed.log')

print(base_path.absolute())  # C:\Users\CSComarch\PycharmProjects\pdnp-18-03-2024\ops_example

print(base_path.name)  # ops_example
print(base_path.parent.absolute())  # C:\Users\CSComarch\PycharmProjects\pdnp-18-03-2024

print(base_path2.suffix)
print(base_path.parts)  # ('ops_example',)
print(base_path2.parts)  # ('ops_example', 'D')

path_test = "ops_example\\A\\D\\ex2.txt"
with open(path_test, 'r', encoding='utf-8') as f:
    data = f.read()
print(data)  # Jakaś treść pliku ex2.txt
