speed_petya = float(input())
speed_vasya = float(input())
speed_tolya = float(input())

if speed_vasya < speed_petya > speed_tolya and speed_vasya > speed_tolya:
    print('1. Петя \n' '2. Вася \n' '3. Толя')
elif speed_petya < speed_vasya > speed_tolya and speed_petya > speed_tolya:
    print('1. Вася \n' '2. Петя \n' '3. Толя')
elif speed_petya < speed_tolya > speed_vasya and speed_vasya > speed_petya:
    print('1. Толя \n' '2. Вася \n' '3. Петя')
elif speed_petya < speed_vasya > speed_tolya and speed_tolya > speed_petya:
    print('1. Вася \n' '2. Толя \n' '3. Петя ')
elif speed_petya < speed_tolya > speed_vasya and speed_petya > speed_vasya:
    print('1. Толя \n' '2. Петя \n' '3. Вася ')
elif speed_tolya < speed_petya > speed_vasya and speed_tolya > speed_vasya:
    print('1. Петя \n' '2. Толя \n' '3. Вася ')
