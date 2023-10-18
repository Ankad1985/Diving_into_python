# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

items = {
    'ключи': 0.3,
    'кошелек': 0.2,
    'телефон': 0.5,
    'зажигалка': 0.1
}
max_weight = 1
backpack = {}
total_weight = 0

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

    
print(backpack)


# for i, weight in things.items():
#     if total_weight + weight <= max_weight:
#         backpack.append(i, weight)
#         total_weight += weight

# print('Берем с собой: ')
# for i in backpack:
#     print(i)
