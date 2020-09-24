revenue = int(input("insert revenue: "))
cost = int(input("insert cost:"))

if revenue < cost:
    print("negative financial result.")
    print(f"damage : {cost - revenue}")
else:
    print("positive financial result.")
    profit = revenue - cost
    print(f"profit : {profit}")
    print(f"profitability : {profit / revenue:.4f}")

    num_of_staff = int(input("\ninsert number of staff:"))
    print(f"profit per staff: {profit / num_of_staff:.4f}")


