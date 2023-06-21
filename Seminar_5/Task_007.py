# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_prime(num):
    if num == 1 or num % 2 == 0:
        return False

    d = 3
    while d*d <= num and num % d != 0:
        d += 2
    return d*d > num


def num_generator(n: int):
    for i in range(0, n+1):
        if i == 0:
            yield 2
        if is_prime(i+2):
            yield i+2


l = num_generator(10)

print(next(l))
print(next(l))
print(next(l))
print(next(l))
