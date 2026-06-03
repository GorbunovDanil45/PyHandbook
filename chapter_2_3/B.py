line: str = input()
count: int = 0
target: str = "зайка"
the_end: str = "Приехали!"

while line != the_end:
    if target in line:
        count += 1
    line = input()
print(count)
