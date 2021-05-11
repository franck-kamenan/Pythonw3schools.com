print(10 > 9)
print(10 == 9)
print(10 < 9)
print(bool(10 > 9))

# True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# __len__ function
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# isinstance function
x = 200
print(isinstance(x, int))