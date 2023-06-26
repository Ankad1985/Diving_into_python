# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def group_rename_files(final_name, num_digits, source_extension, target_extension, name_range):
    directory = "."

    files = os.listdir(directory)

    filtered_files = [file for file in files if file.endswith(
        source_extension) and len(file) >= name_range[1]]

    filtered_files.sort()

    file_counter = 1

    for file in filtered_files:

        original_name = file[name_range[0] - 1:name_range[1]]

        counter_string = str(file_counter).zfill(num_digits)

        new_name = original_name + final_name + counter_string + target_extension

        os.rename(os.path.join(directory, file),
                  os.path.join(directory, new_name))

        file_counter += 1


group_rename_files("_new", 4, ".txt", ".docx", [3, 6])
