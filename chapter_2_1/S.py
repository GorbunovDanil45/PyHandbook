n = Чек
name_product = str(input())
price = int(input())
weight = int(input())
money = int(input())

total_price = price * weight
change = money - price * weight

print(f'{n:<35}\n'
      f'Товар: {name_product:>35}\n'
      f''Цена: '{weight}'кг'' * '{price}'руб/кг: < 35'\n'
      f'{'Итого:':<35}{total_price}{'руб'}\n'
      f'{'Внесено:':<35}{money}{'руб'}\n'
      f'{'Сдача:':<35}{change}{'руб'}\n'
      f'{'=':=>35}')
