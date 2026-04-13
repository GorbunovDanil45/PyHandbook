number = int(input())

hundreds = number // 100
dozens = number // 10 % 10
units = number % 10

high = max(hundreds, dozens, units)
low = min(hundreds, dozens, units)
middle = (hundreds + dozens + units) - high - low

max_digit = high * 10 + middle

if low == 0:
    min_digit = middle * 10 + low
else:
    min_digit = low * 10 + middle

print(f'{min_digit} {max_digit}')
