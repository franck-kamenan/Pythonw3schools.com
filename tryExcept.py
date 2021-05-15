# Exception Handling
try:
  print(x) # The try block will generate an error, because x is not defined
except:
  print("An exception occurred")

# Many Exceptions
try:
  print(x) # The try block will generate a NameError, because x is not defined
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") # The try block does not raise any errors, so the else block is executed

# Finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") # The finally block gets executed no matter if the try block raises any errors or not

# Raise an exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")