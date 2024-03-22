import os

print(os.path.abspath('start.py'))
# C:\Users\CSComarch\PycharmProjects\pdnp-18-03-2024\start.py

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        # print(files)
        for filename in files:
            print(filename)
