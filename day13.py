# def login_required(func):
#     def wrapper(*args, **kwargs):
#         if not is_logged_in():
#             raise Exception("User must be logged in to access this function.")
#         return func(*args, **kwargs)
#     return wrapper
# @login_required
# def transfer_money(user,amount):
#     print(f"Transferring {amount} to {user}.")
#     @login_required
#     def delete_account(user):
#         print(f"Deleting account for {user}.")
# generators:memory overhead problem solve by 
def get_even_numbers(n):
    for i in range(n):
        if i % 2 ==0:
            yield i 
            evens_generator = get_even_numbers(10)
            print(next(evens_generator))  # Output: 0
            print(next(evens_generator))  # Output: 2   
            print(next(evens_generator))  # Output: 4