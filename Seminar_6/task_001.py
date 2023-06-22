# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

import random as rn
import sys as s
import math as mth

num = rn.randint(1, 10)
print(num)

a_cos = mth.acos(0.5)
print(a_cos)

s.exit()
