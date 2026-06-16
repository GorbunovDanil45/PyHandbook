number: int = int(input())
max_digit: int = 0

while number > 0:
    last_digit = number % 10
    if last_digit > max_digit:
        max_digit = last_digit

    number = number // 10

print(max_digit)
