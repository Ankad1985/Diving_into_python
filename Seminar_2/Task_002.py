# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

data = [4, 6.0, 'String', False, False, 6]
number = 1
integer = ''
string = ''
for i in data:
    if isinstance(i, int):
        integer = 'integer'
    if isinstance(i, str):
        integer = 'String'
    print('number: ', number, ' var: ', i, ' type: ', type(i), ' id: ', id(
        i), ' hash: ', hash(i), ' integer: ', integer, ' string', string)
    number += 1
    integer = ''
