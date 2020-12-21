#Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.


def cut_rect (a, b, mas):
    nsquare = 0
    if a == b:
        print('Длинна ребра: ' + str(a))
        print('Квадрат площадью: ' + str(a*a))
        mas.append(a)
        return mas
    elif a < b:
        print('Длинна ребра: ' + str(a))
        print('Квадрат площадью: ' + str(a*a))
        mas.append(a)
        b -= a
    else:
        print('Длинна ребра: ' + str(b))
        print('Квадрат площадью: ' + str(b*b))
        mas.append(b)
        a -= b
    return cut_rect(a, b, mas)

mas = []
a = int(input('Введите сторону a: '))
b = int(input('Введите сторону b: '))
mas = cut_rect(a, b, mas)
print('Массив сторон квадратов: \n' + str(mas))
nsquare = len(mas)
print('Колличество квадратов: ' + str(nsquare))
symb = 0
print('Первый символ массива: ' + str(symb))
for i in mas:
    mas_squares = []
    for j in range(i):
        mas_squares.append(symb)
    for n in range(i):
        print(mas_squares)
    symb += 1
    print(" ")
