product = input()
price = int(input())
weight = int(input())
banknotes = int(input())

print(f"{'Чек':=^35}")
print(f'Товар:{product: >29}')

line_3 = f'{weight}кг * {price}руб/кг'
print(f'Цена:{line_3: >30}')

line_4 = f'{weight * price}руб'
print(f'Итого:{line_4: >29}')

line_5 = f'{banknotes}руб'
print(f'Внесено:{line_5: >27}')

line_6 = f'{banknotes - weight * price}руб'
print(f'Сдача:{line_6: >29}')

print(f"{'=':=^35}")
