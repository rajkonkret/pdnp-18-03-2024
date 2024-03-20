def allparams(a, b, /, c=42, d=256):
    print("a, b", a, b)
    print("c, d", c, d)


# ile minniumu arg?
allparams(1, 2)
allparams(1, 2, 3)
allparams(1, 2, c=3)


# allparams(b=7, a=9, c=6)  # TypeError: allparams() got some positional-only arguments passed as keyword arguments: 'a, b'
# / oddziela argumnty które musza byc przekazane po pozycji od pozostałych
# a i b muszą byc po pozycji
# c i d moga byc również jako nazwane
def allparams2(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams2(1, 2)
allparams2(1, 2, 3)  # c, d 3 256
allparams2(1, 2, 3, 4)  # c, d 3
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)  # args (4, 5, 6, 7, 8, 9, 10, 11)
# d musi byc po nazwie
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, d=90)  # args (4, 5, 6, 7, 8, 9, 10, 11) # c, d 3 90
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, d=90, a=7)  # kwargs {'a': 7}
