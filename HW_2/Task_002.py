# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

str_1 = input('Введите первую строку вида "a/b": ')
str_2 = input('Введите вторую строку вида "a/b": ')
str_1_split = str_1.split('/')
str_2_split = str_2.split('/')

numerator_1 = int(str_1_split[0])
denominator_1 = int(str_1_split[1])
numerator_2 = int(str_2_split[0])
denominator_2 = int(str_2_split[1])

sum_fract = (numerator_1 / denominator_1) + (numerator_2 / denominator_2)
multi_fract = (numerator_1 / denominator_1) * (numerator_2 / denominator_2)

print(
    f'Результат: \n Сумма дробей: {sum_fract}, Произведение дробей: {multi_fract}')

fract_1 = fractions.Fraction(numerator_1, denominator_1)
fract_2 = fractions.Fraction(numerator_2, denominator_2)
sum = fract_1 + fract_2
multi = fract_1 * fract_2

print(
    f'Проверка: \n Сумма: {sum}, Произведение: {multi}')
