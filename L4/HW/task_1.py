# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


def get_wage_func(hours, rate, bonus):
    return hours * rate + bonus


try:
    wage = get_wage_func(int(argv[1]), int(argv[2]), int(argv[3]))
    print(f"wage = {wage}")
except ValueError:
    print("wrong type of param")
except TypeError:
    print("wrong type of param")
except IndexError:
    print("wrong num of param")


