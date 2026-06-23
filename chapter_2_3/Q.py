number: int = int(input())
new_number: int = 0 # переменная, в которую будет записываться новое число
digit: int = 1 # переменная, которая будет означать разряды и с каждой итерацией умножаться на 10

while number > 0:
    last_digit = number % 10 
    if last_digit % 2: # сокращенная запись if last_digit % 2 != 0
        new_number += last_digit * digit
        digit *= 10
    else:
        pass
    number //= 10

print(new_number)
