number = int(input('Введите номер кармана (0-36) '))
if number == 0:
    print('Карман зеленый')
elif number >=1 and number <=10:
    if number % 2 == 0:
        print('Карман черный')
    else:
        print('Карман красный')
elif number >=11 and number <=18:
    if number % 2 == 0:
        print('Карман красный')
    else:
        print('Карман черный')
elif number >=19 and number <=28:
    if number % 2 == 0:
        print('Карман черный')
    else:
        print('Карман красный')
elif number >=29 and number <=36:
    if number % 2 == 0:
        print('Карман красный')
    else:
        print('Карман черный')
else:
    print('Ошибка ввода')



