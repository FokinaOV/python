# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def mult_even_num_func(range_start, range_stop):
    num_list = [el for el in range(range_start, range_stop + 1) if el % 2 == 0]
    return reduce(lambda a, b: a * b, num_list)


print(mult_even_num_func(100, 1000))
