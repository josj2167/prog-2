#!/usr/bin/python3
from person import Person

# Create a Person object with an age
f = Person(5)

# Use the available methods in the Person class
age = f.get()  # Use the get method to get the age
print("Age:", age)

f.set(9)  # Use the set method to change the age

# If the Fibonacci function is available in the Person class, call it
# However, make sure to use the correct method name based on the class definition in person.py
# For example, if the method is named 'fibonacci' in the Person class:
fib_result = f.fibonacci()
print("Fibonacci Result:", fib_result)