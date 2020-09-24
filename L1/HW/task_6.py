first_km = int(input("insert km in first day: "))
last_km = int(input("insert desired km: "))

day = 1
while first_km < last_km:
    first_km = first_km * 1.1
    day += 1
    print(f"in {day} day : {first_km:.2f} km")

print(f"in {day} day result not less then {last_km}")
