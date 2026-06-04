price: float = float(input())
result: float = 0.0

while price != 0:
    if price >= 500:
        price = price * 0.9
    result = price + result
    price: float = float(input())    

print(result)
