# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_name = {1: "january",
              2: "february",
              3: "march",
              4: "april",
              5: "may",
              6: "june",
              7: "july",
              8: "august",
              9: "september",
              10: "october",
              11: "november",
              12: "december"}

season_winter = [12, 1, 2]
season_spring = [3, 4, 5]
season_summer = [6, 7, 8]
season_autumn = [9, 10, 11]

user_ans = int(input("insert number of month: "))

if user_ans in season_winter:
    season_name = "winter"
elif user_ans in season_spring:
    season_name = "spring"
elif user_ans in season_summer:
    season_name = "summer"
elif user_ans in season_autumn:
    season_name = "autumn"
else:
    season_name = "unknown"

print(f"This is {season_name} month ({month_name.get(user_ans)})")
