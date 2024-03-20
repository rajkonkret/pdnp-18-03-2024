# context manager (with)

# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file anokd open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Jeszcze jedno\n")

with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")

# with open('test.log', 'x') as f:
#     f.write("Test")  # FileExistsError: [Errno 17] File exists: 'test.log' bo opcja x

with open('test.log', 'a', encoding='utf-8') as file:
    file.write("dodane\n")
    file.write("dodane\n")
    file.write("dodane\n")
    file.write("dośdane\n")
    file.write("dośćńdane\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
