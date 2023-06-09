# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

from collections import Counter

my_lst = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7]
new_lst = Counter(my_lst)
#print(new_lst)
result_lst = []
for element, count in new_lst.items():
    if count > 1:
        result_lst.append(element)

print(result_lst)
