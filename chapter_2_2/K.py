number = int(input())

a = number // 100
b = number // 10 % 10
c = number % 10

if a < b > c and a > c and b + c == a * 2:
    print('YES')

elif b < a > c and b > c and a + c == b * 2:
    print('YES')

elif b < c > a and b > a and c + a == b * 2:
    print('YES')

elif a < c > b and a > b and c + b == a * 2:
    print('YES')

elif c < a > b and c > b and a + b == c * 2:
    print('YES')

elif c < b > a and c > a and b + a == c * 2:
    print('YES')

else:
    print('NO')
