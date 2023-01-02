# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

# day_week = (int(input('Введите цифру, обозначающую день недели: ')))
# if day_week in (6, 7):
#     print ('Да этот день выходной')
# elif day_week in (1, 2, 3, 4, 5):
#     print('Нет, этот день недели не выходной')
# else:
#     print('Нет такого дня недели')

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

# for x in True, False:
#     for y in True, False:
#         for z in True, False:
#             print(f' x = {x} y = {y} z = {z}', end= ' -> ')
#             print(not (x and y and z) == (not x) or (not y) or (not z))


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_nums(n):
    xy = ['x', 'y']
    a = []
    for i in range(n):
        a.append(int(input(f'Введите координаты ({xy[i]}): ')))
    return a

def area_num(xy):
    area = 4
    if xy[0] > 0 and xy[1] > 0:
        area = 1
    elif xy[0] < 0 and xy[1] > 0:
        area = 2
    elif xy[0] < 0 and xy[1] < 0:
        area = 3
    return area

print(f'Эти координаты попадают в {area_num(input_nums(2))} четверть')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21