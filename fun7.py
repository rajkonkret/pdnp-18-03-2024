def connect(**opcje):  # ** - argumenty słownikowe, nazwane
    print(opcje)
    conect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    conect_param['pwd'] = opcje
    print(conect_param)


def all_args(*args, **kwargs):
    print(args, kwargs)


connect()
connect(a=7)  # argument nazwany wyglada na para klucz-wartosc, {'a': 7}
connect(name="Radek")  # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'name': 'Radek'}}
connect(a=8, name="radek", opt=True)
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 8, 'name': 'radek', 'opt': True}}

all_args()  # () {}
all_args(1, 2, 3)  # (1, 2, 3) {}
all_args(a=1, b=2, c=3)  # () {'a': 1, 'b': 2, 'c': 3}
# all_args(a=1, 2)  # SyntaxError: positional argument follows keyword argument
all_args(None)  # (None,) {}
