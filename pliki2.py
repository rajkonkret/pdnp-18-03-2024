import chardet
# pip install chardet

file_path = 'test.log'
with open(file_path, 'rb') as file:  # musi byc odczytany w trybie binarnym rb
    raw_data = file.read()

# print(raw_data)  # b'Radek\r\ndodane\r\ndodane\r\ndodane\r\ndo\xc5\x9bdane\r\n'
result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.670697820753897, 'language': 'Turkish'}
# po zwiększeniu próbki
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
print(type(result))  # <class 'dict'>
confidence = result['confidence']
print(confidence)
encoding = result['encoding']
print(encoding)  # utf-8
print(raw_data.decode(encoding=encoding))
# Radek
# dodane
# dodane
# dodane
# dośdane
# dośćńdane
