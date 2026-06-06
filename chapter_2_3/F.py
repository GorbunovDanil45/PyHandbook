number_1: int = int(input())
number_2: int = int(input())

low_num = min(number_1, number_2)
high_num = max(number_1, number_2)

while low_num:
    high_num, low_num = low_num, high_num % low_num

print(high_num)
