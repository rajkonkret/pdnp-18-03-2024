import pandas as pd

excel_data = pd.read_excel('sales.xlsx')
print(excel_data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

data = pd.DataFrame(excel_data)
# data = pd.DataFrame(excel_data, columns=['Sales Date', 'Sales Person'])  # wczytanie tylko wybranych kolumn
print(data)
print(data.values)
print(data.columns)  # Index(['Sales Date', 'Sales Person', 'Amount'], dtype='object')
print(data.items)
print(data.index[-1])  # 3
# <bound method DataFrame.items of   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000>

print(data.columns[0])  # Sales Date
print(data[data['Amount'] > 48000])  # filtrowanie wierszy
# Sales Date
#   Sales Date Sales Person  Amount
# 0 2018-05-12   Sila Ahmed   60000
# 1 2019-12-06  Mir Hossain   50000
