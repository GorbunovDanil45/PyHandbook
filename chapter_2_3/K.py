number: int = int(input())

total_sum: int = 0

while number > 0:
    last_digit = number % 10
    total_sum = total_sum + last_digit
    number = number // 10

print(total_sum)
