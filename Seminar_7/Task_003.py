# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def something_strange(new_file):
    massive_multiplied_numbers = []
    massive_of_names = []
    lenght_of_first_file = 0
    lenght_of_second_file = 0

    with (
        open('file.txt', 'r', encoding='utf-8') as f1,
        open('file_with_name.txt', 'r', encoding='utf-8') as f2,
        open(new_file, 'w', encoding='utf-8') as f3

    ):
        while numbers := f1.readline():
            int_number, float_number = numbers.strip().split("|")
            massive_multiplied_numbers.append(
                int(int_number) * float(float_number))
            lenght_of_first_file += 1
        while name := f2.readline():
            massive_of_names.append(name)
            lenght_of_second_file += 1

        lenghts = sorted([lenght_of_first_file, lenght_of_second_file])

        for i in range(lenghts[0]):
            if massive_multiplied_numbers[i] < 0:
                f3.write(massive_of_names[i].lower(
                ) + str(abs(massive_multiplied_numbers[i])) + "\n")
            else:
                f3.write(massive_of_names[i].upper(
                ) + str(round(massive_multiplied_numbers[i])) + "\n")

        for i in range(lenghts[1] - lenghts[0]):
            if massive_multiplied_numbers[i] < 0:
                f3.write(massive_of_names[i].lower(
                ) + str(abs(massive_multiplied_numbers[i])) + "\n")
            else:
                f3.write(massive_of_names[i].upper(
                ) + str(round(massive_multiplied_numbers[i])) + "\n")


something_strange("appended_file.txt")
