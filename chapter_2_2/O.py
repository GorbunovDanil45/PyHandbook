number_1 = int(input())
number_2 = int(input())

tens_1 = number_1 // 10
units_1 = number_1 % 10
tens_2 = number_2 // 10
units_2 = number_2 % 10

high_digit = max(tens_1, units_1, tens_2, units_2)
low_digit = min(tens_1, units_1, tens_2, units_2)

middle_digit = ((tens_1 + units_1 + tens_2 + units_2) - high_digit - low_digit) % 10

print(f'{high_digit}{middle_digit}{low_digit}')
