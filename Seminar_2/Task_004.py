# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
from decimal import Decimal, getcontext

getcontext().prec = 42      # общее количества знаков числа


def circle(radius):
    lenght = Decimal(2) * Decimal(radius) * Decimal(math.pi)
    square = Decimal(radius**2) * Decimal(math.pi)

    return lenght, square


radius = float(input('Введите радиус: '))
print(circle(radius))
