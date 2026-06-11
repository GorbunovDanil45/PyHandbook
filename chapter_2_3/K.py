n: int = int(input())

total_sum: int = 0

while n > 0:
    n = n % 10
    total_sum = total_sum + n
    n = n // 10

print(total_sum)
