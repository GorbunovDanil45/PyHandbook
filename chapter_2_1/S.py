name_product = str(input())
price = int(input())
weight = int(input())
money = int(input())

total_price = price * weight
change = money - price * weight

line_1 = 'Чек'
print(f'{line_1:=^35}')

line_2 = name_product
print(f'Товар: {name_product:>28}')

line_3 = f'{weight}кг * {price}руб/кг'
print(f'Цена: {line_3:>29}')

line_4 = f'{total_price}руб'
print(f'Итого: {line_4:>28}')

line_5 = f'{money}руб'
print(f'Внесено: {line_5:>26}')

line_6 = f'{change}руб'
print(f'Сдача: {line_6:>28}')

line_7 = f'='
print(f'{line_7:=^35}')
