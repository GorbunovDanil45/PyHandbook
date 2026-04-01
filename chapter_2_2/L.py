a = int(input())
b = int(input())
c = int(input())

if a < b > c and a + c > b:
    print('YES')

elif b < a > c and b + c > a:
    print('YES')

elif b < c > a and a + b > c:
    print('YES')

elif a == b == c:
    print('YES')

else:
    print('NO')
