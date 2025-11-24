stolbec1, strochka1, stolbec2, strochka2 = map(int, input('Введите столбец, затем строчку сначала первой, потом второй клетки через пробел ').split())

if abs(stolbec1-stolbec2) == abs(strochka1-strochka2):
    print ('YES')
elif stolbec1<1 or stolbec1>8 or stolbec2<1 or stolbec2>8 or strochka1<1 or strochka1>8 or strochka2<1 or strochka2>8:
    print ('Неккоректый ввод')
else:
    print ('NO')