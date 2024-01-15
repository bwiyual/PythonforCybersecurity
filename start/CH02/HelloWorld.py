#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created 

user_name = input("What is your name? ")

print("Hello", user_name + "!")


print("Today is going to be a great day!")


try:
    user_age = int(input("How old are you? "))
    future_age = user_age + 2
    print(f"In 2 years, you will be {future_age} years old.")
except ValueError:
    print("Invalid age input. Please enter a valid number.")
