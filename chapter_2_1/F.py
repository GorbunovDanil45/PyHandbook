product = (input())
price_per_kg = int(input())
weight = int(input())
money = int(input())

print("Чек")

print(f"{product} - {weight}кг - {price_per_kg}руб/кг")

total_price = price_per_kg * weight

print(f"Итого: {total_price}руб")

print(f"Внесено: {money}руб")
change = money - total_price
print(f"Сдача: {change}руб")
