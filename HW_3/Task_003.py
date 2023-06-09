# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

things = {
    'Еда': 7,
    'Пивко': 20,
    'Спальник': 2,
    'Палатка': 3
}
max_weight = 30
backpack = []
total_weight = 0

for i, weight in things.items():
    if total_weight + weight <= max_weight:
        backpack.append(i)
        total_weight += weight
# print(backpack)
print('Берем с собой: ')
for i in backpack:
    print(i)
