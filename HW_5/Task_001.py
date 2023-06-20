# Напишите функцию, которая принимает на вход строку — 
# абсолютный путь до файла. Функция возвращает кортеж из трёх 
# элементов: путь, имя файла, расширение файла.

import os


def split_path(filepath):
    # Получаем абсолютный путь, имя файла и расширение
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    filename_parts = os.path.splitext(filename)
    extension = filename_parts[1]

    # Возвращаем кортеж из трёх элементов
    return path, filename_parts[0], extension


file_path = '/path/to/file.txt'
result = split_path(file_path)
print(result)
