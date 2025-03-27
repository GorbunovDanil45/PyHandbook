name = (input())
wardrobe = int(input())

group_number = wardrobe // 100
list_number = wardrobe % 10
bed_number = wardrobe // 10 % 10

print('Группа №' + str(group_number) + '.\n' + str(list_number) + '. ' + name +
      '.\n' + 'Шкафчик: ' + str(wardrobe) + '.\n' + 'Кроватка: ' + str(bed_number) + '.')
