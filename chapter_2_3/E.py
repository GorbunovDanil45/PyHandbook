price: float = float(input())
result: float = 0

while price != 0:
    price: float = float(input())
    if price >= 500:
        price = price * 0.9
    result += price
    price = float(input())
    
print(result)
