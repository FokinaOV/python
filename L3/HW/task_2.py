# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def person_info_func(name, surname, birthday, city, email, phone):
    return "Person info: " \
           + "Surname: " + surname \
           + ", Name: " + name \
           + ", Birthday: " + birthday \
           + ", City: " + city \
           + ", Phone: " + phone \
           + ", Email: " + email


name = input("insert name: ")
surname = input("inset surname: ")
birthday = input("insert birthday: ")
city = input("insert city: ")
email = input("insert email: ")
phone = input("insert phone: ")

print(person_info_func(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))
