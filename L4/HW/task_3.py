# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


def my_func_20_21(range_start, range_stop):
    return [el for el in range(range_start, range_stop) if el % 20 == 0 or el % 21 ==0]


print(f"numbers that are multiples of 20, 21: {my_func_20_21(20, 240)}")
