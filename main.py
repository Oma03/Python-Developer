"""
There are two types of variables in oop
class variable
instance variable
"""

"""
Inheritance
Inheritance is the ability for a class to get or inherit properties from another class
There are types of inheritance
single level inheritance
multi level inheritance
eg 
"""


# class Parent:
#     def show(self):
#         print("This is the parent class")
#
#
# class Son(Parent):
#     def son_show(self):
#         print("This is the son class")
#
#
# class Grand(Son):
#     def grand_show(self):
#         print("This is the grandchild")
#
#
# patience = Son()
# patience.show()
# patience = Grand()
# patience.son_show()

# single level inheritance


# class Animal:
#     def animal_show(self):
#         print("animal class")
#
#
# class Human(Animal):
#     def human_show(self):
#         print("human class")

# Multi level inheritance

#
# class Animal:
#     def animal_show(self):
#         print("animal class")
#
#
# class Human(Animal):
#     def human_show(self):
#         print("human class")
#
#
# class Dog(Human):
#     def dog_show(self):
#         print("dog class")

# Multiple inheritance


# class Animal:
#     def animal_show(self):
#         print("animal class")
#
#
# class Human:
#     def human_show(self):
#         print("human class")
#
#
# class Dog(Animal, Human):
#     def dog_show(self):
#         print("dog class")


# class Calc:
#     def add(self, num1, num2):
#         return num1 + num2
#
#     def sub(self, num1, num2):
#         return num1 - num2
#
#
# class Calc2(Calc):
#     def mul(self, num1, num2):
#         return num1 * num2
#
#     def divide(self, num1, num2):
#         return num1 / num2
#
#
# casio = Calc2()
# print(casio.add(2, 4))
# print(casio.mul(2, 4))

"""
Task 
Using inheritance, write a class called Time whose only field is a time in seconds.
It should have a method called convert to minutes that returns a string of minutes
and seconds formatted as in he following:
if second is 230, the method should return '5:50'. t should also have a method called 
convert to hours that returns a string of hours minutes and seconds formatted analogously
in the previous method.
"""


# class Time:
#     def __init__(self, sec):
#         self.sec = sec
#
#     def minute(self):
#         if sec > 60:
#             min = self.sec // 60
#             minsec = self.sec % 60
#             print(f"The time is {min} minute(s) : {minsec} seconds")
#         else:
#             print(f"The time is {sec} seconds")
#
#
# class ConvertToHours(Time):
#     def hours(self):
#         if sec >= 3600:
#             hour = self.sec // 3600
#             min = (self.sec % 3600) // 60
#             minsec = self.sec % 60
#             print(f"The time is {hour} hour(s) : {min} minute(s) : {minsec} second(s)")
#
#
# sec = int(input("Enter time in seconds: "))
# swatch = ConvertToHours(sec)
# swatch.minute()
# swatch.hours()


# """
# Write a bankaccount class that has properties of accountno, pin
# and it is going to have a method of withdraw, deposit and checkballance
# """
#

# class BankAccount:
#     def __init__(self, accountno, pin):
#         self.accountno = accountno
#         self.pin = pin
#         self.pin = 2007
#         self.account_balance = 5000
#
#     def withdraw(self, withdrawal_amount):
#         self.account_balance = self.account_balance - withdrawal_amount
#         return "current balance: ", self.account_balance
#
#     def deposit(self, deposit_amount):
#         self.account_balance = self.account_balance + deposit_amount
#         return "current balance: ", self.account_balance
#
#     def checkbalance(self):
#         return "your account balance is: ", self.account_balance
#
#     def checkpin(self):
#         if pin == self.pin:
#             print("Continue")
#         else:
#             print("incorrect pin")

#
# accountno = input("please enter your account number: ")
# pin = input("please enter your pin: ")
# Stanley = BankAccount(accountno, pin)
# if pin == Stanley.pin:
#     print("What do you want to do?")
#     system = print(input("""
#     Withdraw
#     Deposit
#     Check Balance
#     """))
#     if system == Withdraw:
#         withdrawal_amount = print(int(input("How much do you want to withdraw")))
#         print(Stanley.withdraw(withdrawal_amount))
#     elif system == Deposit:
#         deposit_amont = print(int(input("How much do you want to deposit: ")))
#         print(Stanley.deposit(deposit_amont))


# ENCAPSULATION


# class HiiT:
#     def __init__(self):
#         self.__name1 = "leo"
#         self.name2 = "patience"
#         self.name3 = "lamido"
#
# # To encapsulate you use the double underscore __. __ is private and one underscore is protected.
# # To show a variable that is encapsulated with double underscore, you have to create another
# # function and return it.
#
#     def show_name1(self):
#         print("Parent")
#
# # To show a protected encapsulation, you create a class that will inherit the attribute.
#
#
# # class Hiit1(HiiT):
# #     def __init__(self):
# #         return self._name1
#
#
# class hitt1(HiiT):
#     def __init__(self):
#         self.name1 = "fj"
#         self.name2 = "brb"
#         self.name3 = "lipo"
#
#     def show_name1(self):
#         super().show_name1()
#         print("child class")
#
#
#
#
# hiit = hitt1()
# hiit.show_name1()

#   def __init__(self):
#          return self._name1
#
#
# class history1(History):
#     def __innit__(self):
#      self.name1 = "Bnakz"
#      self.name2 = "annie"
#      self.name3 = "canon"
#      self.name4 = "name"
#
# def show_name1(self):
#  super().show_name1()
#  print("parent class")

# TASK
# class Method:
#     def print_string(self, get_string):
#        return get_string.upper()
#
#
# get_string = input("What is the string: ")
# methods = Method()
# print(methods.print_string(get_string))

# OR
# class Method:
#     def get_string(self, get_strings):
#         return get_strings
#
#     def print_string(self, get_strings):
#         print_strings = get_strings.upper()
#         return print_strings
#
# get_strings = input("Enter a string: ")
# methods = Method()
# print(methods.print_string(get_strings))
# print(methods.get_string(get_string))

"""
Polymorphism
ability for a class or an object to behave in multiple forms.
"""


# class name1:
#     def display(self):
#         print("display name")
#
#
# class name2():
#     def display(self):
#         print("display name2")
#
#
# name = name2()
# name.display()

"""
open() is a keyword used in opening files in python.
"""
#
# myfile = open("names.txt", "r")
# mytect = myfile.read()
# for x in mytect:
#     print(x, end=" ")
# myfile.close()

# myfile = open("login.txt", "a")
# username = input("Enter a name: ")
# myfile.write(username)
# login = input("Enter your login name: ")
# if login == username:
#     print("You are welcome")
# else:
#     print("Wrong login")
# myfile.close()

