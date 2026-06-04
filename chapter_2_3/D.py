number_1: int = int(input())
number_2: int = int(input())

if number_1 < number_2:
    for i in range(number_1, number_2 + 1):
        print(i, end=" ")
else:
    for i in range(number_1, number_2 - 1, - 1):
        print(i, end=" ")
