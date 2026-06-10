a: int = 0
b: int = 0

end: str = "СТОП"

course: str = input()

while course != end:
    steps: int = int(input())

    match course:
        case 'СЕВЕР':
            a = a + steps
        case 'ЮГ':
            a = a - steps
        case 'ВОСТОК':
            b = b + steps
        case 'ЗАПАД':
            b = b - steps
    course = input()

print(f"{a}\n{b}")
