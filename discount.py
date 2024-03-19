from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2024-03-19

time = datetime.now()
print(time)  # 2024-03-19 15:03:41.549154

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-03-20

print(time.hour)  # 15
print(today.day)  # 19

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 19/03/2024

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 15:08

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': tomorrow, 'price': 80.0},
    {'sku': 3, 'exp_date': today, 'price': 250},
    {'sku': 4, 'exp_date': today, 'price': 150},
    {'sku': 5, 'exp_date': today, 'price': 250},
    {'sku': 6, 'exp_date': tomorrow, 'price': 200},
    {'sku': 7, 'exp_date': today, 'price': 250},
]

for product in products:
    # print(product)  # {'sku': 1, 'exp_date': datetime.date(2024, 3, 19), 'price': 100}
    if product['exp_date'] != today:
        continue  # nic nie rób z tym elementem, każ pętli podstawić następny
    product['price'] *= 0.8  # p = p * 0.8
    print(f"""
    Price for sku {product['sku']}
    is now {product['price']}""")
