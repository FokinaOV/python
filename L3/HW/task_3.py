# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(val_1, val_2, val_3):
    if val_1 > val_2 and val_1 > val_3:
        max_1 = val_1
        if val_2 > val_3:
            max_2 = val_2
        else:
            max_2 = val_3
    elif val_2 > val_1 and val_2 > val_3:
        max_1 = val_2
        if val_1 > val_3:
            max_2 = val_1
        else:
            max_2 = val_3
    else:
        max_1 = val_3
        if val_1 > val_2:
            max_2 = val_1
        else:
            max_2 = val_2
    return max_1 + max_2


print(my_func(1, 2, 3))
print(my_func(1, 3, 2))
print(my_func(2, 1, 3))
print(my_func(2, 3, 1))
print(my_func(3, 1, 2))
print(my_func(3, 2, 1))
