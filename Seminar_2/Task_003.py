# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает 
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего 
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода 
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# def gonext(num, system):
#     res = 0
#     ost = 0
#     resString = ''
#     while True:
#         res = num // system
#         ost = num % system
#         if res < system:
#             resString = resString + str(ost) + str(res)
#             break
#         else:
#             num = res
#             resString = resString + str(ost)
#     return resString[::-1]

# integer = int(input('Введите целое число: '))
# print(gonext(integer, 2))

integer = int(input("Введите целое число: "))

def trans(integer, system):
    res = 0
    support = 10
    power = 0
    while integer > 0:
        res += (integer % system) * (support**power)
        power += 1
        integer = integer // system
    return res

print(trans(integer, 8))

# проверка
print(trans(integer, 8) == int(oct(integer)[2:]))       # [2:] - срез