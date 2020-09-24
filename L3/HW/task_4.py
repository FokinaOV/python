# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func_1v(x, y):
    return x ** y


def my_func_2v(x, y):
    x_2 = x
    for i in range(1, abs(y)):
        x_2 *= x
    return 1 / x_2


try:
    val_x = float(input("insert float: "))
    val_y = int(input("insert int: "))
    print(my_func_1v(val_x, val_y))
    print(my_func_2v(val_x, val_y))
except ValueError:
    print("wrong value")
