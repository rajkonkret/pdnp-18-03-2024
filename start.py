# import fun1  # importuje plik
import pakiet  # importuje z pakietu metody na które zezwala __init_.py
import pakiet.fun as pk  # importuje z pakietu cały plik jako alias
from pakiet import fun  # importoje plik z pakietu

# fun1.dodaj2(7, 8)
pakiet.powitanie()  # po dodaniu w __init_.py
pk.powitanie()  # nie ma potrzeby umiesczac w __init__.py
fun.powitanie()
# info() nie znajduje się w __init__.py
# pakiet.info()  # AttributeError: module 'pakiet' has no attribute 'info'
# inport bezpośredni pliku zadziała
pk.info()
fun.info()
