# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division_func(val_1, val_2):
    try:
        return val_1 / val_2
    except ZeroDivisionError:
        return


try:
    value_1 = float(input("insert first number: "))
    value_2 = float(input("insert second number: "))
    print(f"result: {value_1} / {value_2} = {division_func(value_1, value_2)}")
except ValueError:
    print("wrong value")
