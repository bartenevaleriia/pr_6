temperature, pressure, pulse = map(float, input('Введите через пробел: температуру(°C), давление (верхнее), пульс (уд/мин)').split())
if (38 < temperature < 35) or (140 < pressure < 105) or (110 < pulse < 55):
    print('Требуется врач')
elif (35 < temperature < 36) or (37 < temperature < 38) or ( 105 < pressure < 130) or (130 < pressure < 140) or (55 < pulse < 60) or (100 < pulse < 110):
    print('Легкое недомогание')
else:
    print('Нормальное состояние')