target: str = "зайка"
count: int = 0
for _ in range(int(input())):
    line: str = input()
    if target in line:
        count += 1

print(count)
