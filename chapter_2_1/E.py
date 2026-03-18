price = int(input())
weight = int(input())
banknotes = int(input())

total_price = price * weight
change = banknotes - total_price
print(change)
