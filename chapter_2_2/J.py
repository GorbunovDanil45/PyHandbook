code = int(input())

a = code // 100
b = code // 10 % 10
c = code % 10

first_pair = a + b
second_pair = b + c

if first_pair > second_pair:
    print(f'{first_pair}{second_pair}')
else:
    print(f'{second_pair}{first_pair}')