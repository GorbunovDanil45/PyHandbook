product_name = input()
price = int(input())
weight = int(input())
banknotes = int(input())

total_price = weight * price

change = banknotes - weight * price

print("Чек")
print(f"{product_name} - {weight}кг - {price}руб/кг")
print(f"Итого: {total_price}руб")
print(f"Внесено: {banknotes}руб")
print(f"Сдача: {change}руб")
