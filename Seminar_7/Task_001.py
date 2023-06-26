#  Напишите функцию, которая заполняет файл 
# (добавляет в конец) случайными парами чисел. 
# ✔ Первое число int, второе - float разделены вертикальной чертой. 
# ✔ Минимальное число - -1000, максимальное - +1000. 
# ✔ Количество строк и имя файла передаются как аргументы функции. 

import random

def new_file(strings_number, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range(strings_number):
            input_numbers = (str(random.randint(-1000, 1000)), str(random.uniform(-1000,1000)))
            f.write("|".join(input_numbers) + "\n")

new_file(10, "file.txt")