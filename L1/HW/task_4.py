source_num = int(input("insert integer: "))


max_num = 0
array_num = []
while source_num > 0:
    if max_num < source_num % 10:
        max_num = source_num % 10
    source_num = source_num // 10

print(f"max num : {max_num}")

