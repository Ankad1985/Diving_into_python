# Напишите функцию, которая генерирует 
# псевдоимена. 
# ✔ Имя должно начинаться с заглавной буквы, 
# состоять из 4-7 букв, среди которых 
# обязательно должны быть гласные. 
# ✔ Полученные имена сохраните в файл.

import random

def names_generator():
    name_lenght = random.randint(4,7)
    letters = "ауойфсжтфорллыивиыдивиыдвлиыи"
    created_name = []
    for i in range(name_lenght // 2):
        letter = random.choice(letters[:9])
        created_name.append(letter)
    for i in range(name_lenght // 2, name_lenght):
        letter = random.choice(letters[10:])
        created_name.append(letter)
    random.shuffle(created_name)

    return "".join(created_name).title()

def write_names(file_name, number_of_names):
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range(number_of_names):
            f.write(names_generator() + "\n")

write_names("file_with_names.txt", 10)
# print(names_generator())
# print(names_generator())
# print(names_generator())
# print(names_generator())
# print(names_generator())        