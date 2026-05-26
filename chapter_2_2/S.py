x, y = float(input()), float(input())

if x >= 0 and y >= 0:
    circle_danger = (x ** 2 + y ** 2 <= 25)
else:
    circle_danger = True
    
if 3 * y <= 5 * x + 35 and y <= 5 and circle_danger and (x + 1) ** 2 - 36 <= 4 * y:
    print("Опасность! Покиньте зону как можно скорее!")
elif x ** 2 + y ** 2 <= 100:
    print("Зона безопасна. Продолжайте работу.")
else:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
