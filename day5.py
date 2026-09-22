# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()
# n= 6
# for i in range(1,n+1):
#     for j in range(1,i+1) :
#         print("*", end=" ")
#     print()
# for i in range(5):
#     print("*" * (i + 1))
# n = 14
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# total_stars = 14
# stars_printed = 0
# row = 1
# while stars_printed < total_stars:
#     for j in range(row):
#         if stars_printed < total_stars:
#             print("*", end=" ")
#             stars_printed += 1
#     print()
#     row += 1
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False