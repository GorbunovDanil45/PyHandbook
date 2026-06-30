number: int = int(input())

temp_number = number
revers_number: int = 0

while number != 0:
    last_digit = number % 10
    revers_number = revers_number * 10 + last_digit
    number = number // 10

if revers_number == temp_number:
    print('YES')

else:
    print('NO')
