low: int = 1
high: int = 1000
more: str = 'Больше'
fewer: str = 'Меньше'
target: str = 'Угадал!'

while True:
    guess = (low + high) // 2
    print(guess)
    reply: str = input()
    if reply == fewer:
        high = guess - 1
    elif reply == more:
        low = guess + 1
    else:
        break
    