a: int = int(input())
b: int = int(input())

high_num = max(a, b)
low_num = min(a, b)

while low_num != 0:
    high_num, low_num = low_num, high_num % low_num
    lcm = (a * b) / high_num #lcm - Least Common Multiple

print(int(lcm))
