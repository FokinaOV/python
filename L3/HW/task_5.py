# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_func(number_list):
    total = 0
    for el in number_list:
        try:
            total += int(el)
        except ValueError:
            return 0
    return total


total_sum = 0
quit_key = "q"
quit_ans = True
while quit_ans:
    user_ans = input("insert numbers(for exit insert \"q\")")
    num_list = user_ans.split(" ")
    if quit_key in num_list:
        quit_ans = False
        index = num_list.index(quit_key)
        num_list = num_list[:index]
    total_sum += sum_func(num_list)
    print(total_sum)



