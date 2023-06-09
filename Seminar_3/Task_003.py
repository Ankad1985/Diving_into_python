# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

tup = (2, 3, 4, 5)


new_dict = {}
for item in tup:
    new_dict.setdefault(type(item), [])
    new_dict[type(item)].append(item)

print(new_dict)
