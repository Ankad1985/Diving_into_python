def num_to_hex(num):
    result = ''
    h = '0123456789ABCDF'
    while num > 0:
        result = h[num % 16] + result
        num = num // 16
    return result


num = int(input('Введите число: '))
print(num_to_hex(num))
print('Проверка:',(hex(num)[2:]))