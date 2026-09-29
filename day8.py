# # class College:
# #     def _init_(self,name,loc,num_students):
# #         self.name=name
# #         self.loc=loc
# #         self.num_students=num_students
# #     def display_info(self):
# # Encapsulation: Hiding the internal state of an object and requiring all interaction to be performed through an object's methods.
# class BankAccount:
#     def __init__(self,account_number,account_holder,balance):
#         self.account_number=account_number
#         self.account_holder=account_holder
#         self.__balance=balance  # Private attribute
#         def get_balance(self):
#             return self.__balance
#         def deposit(self,amount):
#             if amount>0:
#                 self.__balance+=amount
#                 print(f"Deposited: {amount}. New balance: {self.__balance}")
#             else:
#                 print("Deposit amount must be positive.")
#                 def withdraw(self,amount):
#                     if 0<amount<=self.__balance:
#                         self.__balance-=amount
#                         print(f"Withdrew: {amount}. New balance: {self.__balance}")
#                     else:
#                         print("Invalid withdrawal amount.")
class Room:
    def __init__(self,room_number,capacity):
        self.room_number=room_number
        self.capacity=capacity
    def display_info(self):
        print(f"Room Number: {self.room_number}, Capacity: {self.capacity}")
#         room1=Room(101,30)
#         room1.display_info()
class Flat:
    def __init__(self,room_number,capacity):
        self.room_number=room_number
        self.capacity=capacity
    def display_info(self):
        print(f"Flat Number: {self.room_number}, Capacity: {self.capacity}")