petya = int(input())
vasya = int(input())
tolya = int(input())

if vasya < petya > tolya and vasya > tolya:
    first = 'Петя'
    second = 'Вася'
    third = 'Толя'
elif petya < vasya > tolya and petya > tolya:
    first = 'Вася'
    second = 'Петя'
    third = 'Толя'
elif petya < tolya > vasya and vasya > petya:
    first = 'Толя'
    second = 'Вася'
    third = 'Петя'
elif petya < vasya > tolya and tolya > petya:
    first = 'Вася'
    second = 'Толя'
    third = 'Петя'
elif petya < tolya > vasya and petya > vasya:
    first = 'Толя'
    second = 'Петя'
    third = 'Вася'
elif tolya < petya > vasya and tolya > vasya:
    first = 'Петя'
    second = 'Толя'
    third = 'Вася'

print(f'{"":8}{first:^8}')
print(f'{second:^8}')
print(f'{"":16}{third:^8}')
print(' II        I        III ')
