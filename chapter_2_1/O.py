N = int(input())
M = int(input())
T = int(input())

Total_minutes = N * 60 + M + T

N1 = Total_minutes // 60 % 24
M1 = Total_minutes % 60

print(f'{N1:0>2}:{M1:0>2}')
