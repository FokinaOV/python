# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

prod_list = list()
user_ans = ""
prod_id = 1
while user_ans != "next":
    name = input("insert name of product: ")
    price = input("insert price: ")
    num = input("insert number of product: ")
    init = input("insert init: ")

    prod_list.append((prod_id, dict(название=name, цена=price, количество=num, eд=init)))
    prod_id += 1
    user_ans = input("for next step insert \"next\":")

print("\nlist of products:")
for el in prod_list:
    print(el)

set_key = set()
for el in prod_list:
    for k in el[1].keys():
        set_key.add(k)

analytics = dict()
for i in set_key:
    set_value = set()
    for j in prod_list:
        value = j[1].get(i)
        if value is not None:
            set_value.add(value)
    analytics[i] = set_value

print("\nanalytics about products: ")
for el in analytics:
    print(f"{el} : {analytics[el]}")
