# Задание №5
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = (2, 5, 6, 3, 2, 5, 6, 4, 6, 8, 9)
new_list = []

for i, item in enumerate(my_list, 1):
    if i % 2 == 1:
        new_list.append(i)

print(new_list)
