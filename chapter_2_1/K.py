number = int(input())

a = number // 100 % 10
b = number // 1000
c = number % 10
d = number // 10 % 10

print(f'{a}{b}{c}{d}')
