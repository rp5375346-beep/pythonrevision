# def cal_total(price, tax_rate, quantity):
#     total = price * quantity * (1 + tax_rate)
#     return total

# # 1. Take inputs from the user
# price = int(input("Enter the price: "))
# tax_rate = float(input("Enter the tax rate (e.g., 0.05 for 5%): "))
# quantity = int(input("Enter the quantity: "))

# # 2. Call the function and store the result
# final_amount = cal_total(price, tax_rate, quantity)

# # 3. Print the calculated result
# print(f"The total amount is: {final_amount}")
# n = int(input("Enter a number: "))
# print(f"The number is: {n}")
# for i in range(1,n+1):
#     print("*", end=" ")
#     if i % 2==0:
#         print()
#     else:
#         print(end=" ")
times_three= make_multiplier (3)
print(times_three(5))  # Output: 15