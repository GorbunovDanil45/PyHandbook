summand1 = int(input())
summand2 = int(input())

n1 = (summand1 // 100 + summand2 // 100) % 10
n2 = (summand1 // 10 % 10 + summand2 // 10 % 10) % 10
n3 = (summand1 % 10 + summand2 % 10) % 10

print(int(f'{n1}{n2}{n3}'))
