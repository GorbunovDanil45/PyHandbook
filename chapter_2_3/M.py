result = chr(0x10ffff)
for _ in range(int(input())):
    name: str = input()
    if name < result:
        result = name

print(result)
