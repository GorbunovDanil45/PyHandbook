N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

x = int((M * N - K2 * N) / (K1 - K2))
y = int(N - x)

print(f'{x} {y}')
