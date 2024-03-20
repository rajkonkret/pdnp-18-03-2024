import pandas

# pip install pandas

data = pandas.read_csv('records2.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3   0.1
# 1  marek    cos     2   8.1
# 2  tomek    cot     1   6.0
# 3  zenek    coy     7  67.4

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['radek' 'coe' 3 0.1]
#  ['marek' 'cos' 2 8.1]
#  ['tomek' 'cot' 1 6.0]
#  ['zenek' 'coy' 7 67.4]]
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3   0.1
# 1  marek    cos     2   8.1
# 2  tomek    cot     1   6.0
# 3  zenek    coy     7  67.4>
