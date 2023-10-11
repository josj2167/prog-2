#!/usr/bin/python3
from person import Person

# Create a Person object with an age
f = Person(5)

# Use the get method to get the age
age = f.get()
print("Age:", age)

# Use the set method to change the age
f.set(9)

# Use the fibonacci method to calculate the Fibonacci number
fib_result = f.fibonacci()
print("Fibonacci Result:", fib_result)