start: int = 1
end: int = int(input())

factorial: int = 1
for i in range(start, end + 1):
    factorial = factorial * i

print(factorial)
