price = (input())
weight = (input())
banknotes = (input())

total_price = price * weight
change = int(banknotes - total_price)
print(change)
