line: str = input()
count: int = 0
target: str = "зайка"
finish: str = "Приехали!"

while line != finish:
    if target in line:
        count += 1
    line = input()
print(count)
