class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Alice", 25)
person.greet()  # Output: Hello, my name is Alice and I am 25 years old.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.area())  # Output: 78.53981633974483
print(circle.circumference())  # Output: 31.41592653589793

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")

account = BankAccount("123456789", 1000)
account.display_balance()  # Output: Account Number: 123456789, Balance: $1000.00
account.deposit(500)
account.display_balance()  # Output: Account Number: 123456789, Balance: $1500.00
account.withdraw(2000)  # Output: Insufficient funds.

#Dictionaries,funtions and classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = {"name": self.name, "age": self.age}

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def get_info(self):
        return self.info

person = Person("Alice", 25)
person.greet()  # Output: Hello, my name is Alice and I am 25 years old.
info_dict = person.get_info()
print(info_dict["name"])  # Output: Alice
print(info_dict["age"])  # Output: 25














