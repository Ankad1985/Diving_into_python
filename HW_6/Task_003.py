# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для 
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и 
# выведите 4 успешных расстановки.

import random

def check_queens(arrangement):
    for i in range(len(arrangement)):
        for j in range(i + 1, len(arrangement)):
            if (
            arrangement[i][0] == arrangement[j][0] or 
            arrangement[i][1] == arrangement[j][1] or 
            abs(arrangement[i][0] - arrangement[j][0]) == abs(arrangement[i][1] - arrangement[j][1])
            ):
                return False
    return True

def generate_arrangement():
    arrangement = []
    for _ in range(8):
        row = random.randint(1, 8)
        column = random.randint(1, 8)
        arrangement.append((row, column))
    return arrangement

successful_arrangements = []
while len(successful_arrangements) < 4:
    arrangement = generate_arrangement()
    if check_queens(arrangement):
        successful_arrangements.append(arrangement)

for i, arrangement in successful_arrangements:
    print(arrangement)


