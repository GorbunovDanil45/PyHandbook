target: int = int(input())
count: int = 0

for number in range(2, int(target ** 0.5) + 1):
    if target % number == 0:
        count += 1
        break

if count == 0 and target > 1:
    print("YES")
else:
    print("NO")
