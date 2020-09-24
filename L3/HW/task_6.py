# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(text):
    return text.title()


def list_func(text_list):
    result_list = list()
    for el in text_list:
        result_list.append(int_func(el))
    return result_list


string = input("insert word: ")
print(int_func(string))

str_list = input("insert text: ")
str_list = str_list.split(" ")
print(list_func(str_list))
