# # num =[5, 10, 15, 20]
# # iterator = iter(num)
# # print(next(iterator))  # Output: 5
# # print(next(iterator))  # Output: 10
# # print(next(iterator))  # Output: 15
# # print(next(iterator))  # Output: 20
# def my_logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function '{func.__name__}' is being called.")
#         result = func(*args, **kwargs)
#         print(f"Function '{func.__name__}' has finished executing.")
#         return result
#     return wrapper
import time
from functools import wraps

# Real World: API Execution Timer & Logger
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) # Runs the actual function
        duration = time.time() - start_time
        print(f"[METRICS] API '{func.__name__}' took {duration:.4f}s to run.")
        return result
    return wrapper

# Applied across your application seamlessly:
@measure_time
def process_payment(user_id, amount):
    # Imagine complex payment gateway API calls here...
    time.sleep(0.5) 
    return "SUCCESS"

process_payment(user_id=402, amount=199.99)