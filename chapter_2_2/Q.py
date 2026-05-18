a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
    
elif a == 0:
    if b == 0:
        print('No solutions')
    else:
        x = -c / b
        if x == 0:
            x = 0.00
        print(f'{x:.2f}')
    
else:
    D = b ** 2 - 4 * a * c

    if D < 0:
        print('No solutions')

    elif D == 0:
        x = -b / (2 * a)
        if x == 0:
            x = 0.00
        print(f'{x:.2f}')

    elif D > 0:
        root_1 = (-b - D ** 0.5) / (2 * a)
        root_2 = (-b + D ** 0.5) / (2 * a)

        x_1 = min(root_1, root_2)
        x_2 = max(root_1, root_2)

        if x_1 == 0:
            x_1 = 0.00
        if x_2 == 0:
            x_2 = 0.00
        print(f'{x_1:.2f} {x_2:.2f}')
