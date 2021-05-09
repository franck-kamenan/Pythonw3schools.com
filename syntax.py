if 5 > 2:
    print("Five is greater than two!")

# This is a comment
"""
This is a comment
written in
more than just one line
"""

# Variables
x = 7
y = "Bye!"
print(x)        # x is of type int
print(y)        # y is of type str
x = "Sally"
print(x)        # x is now of type str

# Casting
x = str(3)
y = int(3)
z = float(3)
print(x)        # x is of type int
print(y)        # x is of type int
print(z)        # x is of type int

# Get the type
print(type(x))
print(type(y))
print(type(z))

# Single or Double Quotes
x = "John"
print(x)
x = 'John'
print(x)

# Case-Sensitive
a = 4
print(a)
A = "Nelly"
print(A)

# Variable Names
myvar = "John"
print(myvar)

# Camel Case
myVariableName = "John"
print(myVariableName)

# Pascal Case
MyVariableName = "John"
print(MyVariableName)

# Snake Case
my_variable_name = "John"
print(my_variable_name)

# assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "awesome"
print("Python is " + x)
x = "Python is "
y = "awesome"
z =  x + y
print(z)
x = 5
y = 10
print(x + y)

# Global and Local Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# create a global variable inside a function
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# change a global variable inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

