seconds = int(input("insert time in seconds: "))

minutes = 0
hours = 0

if seconds > 60:
    minutes = seconds // 60
    seconds = seconds % 60
if minutes > 60:
    hours = minutes // 60
    minutes = minutes % 60

print(f"time in normal form: {hours}:{minutes}:{seconds}")



