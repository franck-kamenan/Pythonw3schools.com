# Create a Class
class MyClass:
  x = 5
print(MyClass)

# Create an Object
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

# The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)

# Delete Object Properties
del p1.age

# Delete Objects
del p1

# The pass Statement
class Person:
  pass # having an empty class definition like this, would raise an error without the pass statement