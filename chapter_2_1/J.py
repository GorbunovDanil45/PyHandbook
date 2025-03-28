name = input()
wardrobe = int(input())

group_number = wardrobe // 100
list_number = wardrobe % 10
bed_number = wardrobe // 10 % 10

print(f'Группа №{group_number}.\n'
      f'{list_number}. {name}.\n'
      f'Шкафчик: {wardrobe}.\n'
      f'Кроватка: {bed_number}.')
