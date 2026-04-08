number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

dozens_1 = number_1 // 10
units_1 = number_1 % 10

dozens_2 = number_2 // 10
units_2 = number_2 % 10

dozens_3 = number_3 // 10
units_3 = number_3 % 10

if dozens_1 == dozens_2 == dozens_3:
    print(dozens_1)
elif units_1 == units_2 == units_3:
    print(units_1)
    