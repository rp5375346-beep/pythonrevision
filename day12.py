# try except else finally
try:
    number=10/2
except ZeroDivisionError:
    print("you cannot divide by zero !")
else:
    print(f"Success! the answer is{number}")
finally:
    print("program finished running.")