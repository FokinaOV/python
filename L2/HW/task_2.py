# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
i = 0
while i <= 10:
    my_list.insert(i, i)
    i += 1

print(f"first list: {my_list}")

for el in my_list:
    indx = my_list.index(el)
    if indx % 2 == 1:
        a, b = indx, indx - 1
        my_list[a], my_list[b] = my_list[b], my_list[a]

print(my_list)
