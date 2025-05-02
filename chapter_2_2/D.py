name_1 = 'Петя'
speed_1 = float(input())
name_2 = 'Вася'
speed_2 = float(input())
name_3 = 'Толя'
speed_3 = float(input())

if speed_1 > speed_2 and speed_1 > speed_3:
    print('1. Петя\n', '2. Вася\n', '3. Толя')
    speed_1, speed_2 = speed_2, speed_1
    name_1, name_2 = name_2, name_1
elif speed_2 < speed_1:
    speed_2, speed_1 = speed_1, speed_2
    name_2, name_1 = name_1, name_2

    print(name_1, name_2, name_3, sep='\n')
