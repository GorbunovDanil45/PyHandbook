a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    x_1 = -(c / b)
    print(f"{x_1:.2f}")
elif a == b == 0:
    print("No solution")
elif a == c == 0:
    print(f"{0:.2f}")
    
else:
    D = (b ** 2) - (4 * a * c)

    if D == 0:
        x_1 = -b / (2 * a)
        print(f"{x_1:.2f}")

    elif D > 0:
        root_1 = (-b - (D ** 0.5)) / (2 * a)
        root_2 = (-b + (D ** 0.5)) / (2 * a)

        x_1 = min(root_1, root_2)
        x_2 = max(root_1, root_2)
        print(f"{x_1:.2f} {x_2:.2f}")

    else:
        print("No solution")
