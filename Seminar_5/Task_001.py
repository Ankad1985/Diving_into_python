# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.

# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

a, b, c, *g = input().split("/")
dict_res = {int(b): int(a), int(c): tuple(map(int,g))}
print(dict_res)
