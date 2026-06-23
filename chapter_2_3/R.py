number: int = int(input())
divisor: int = 2
new_divisor: list = []

while number > 1:
    if number % divisor == 0:
        number //= divisor
        new_divisor += [divisor]
    else:
        divisor += 1

print(*new_divisor, sep=' * ')
