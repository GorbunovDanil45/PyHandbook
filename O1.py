N = int(input())
M = int(input())
T = int(input())

hour = (T // 60 % 24 + N) % 24 + (M + T % 60) // 60
minutes = (M + T % 60) % 60

print(f"{hour:02}:{minutes:02}")