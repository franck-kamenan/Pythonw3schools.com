thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Length
print(len(thistuple))

# tuple with only one item
thistuple = ("apple",)
print(type(thistuple))

# Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

# 1 tuple can contain different data type
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)

# type()
print(type(tuple4))

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Access Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])

# Negative Indexing
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:5])
print(thistuple[2:])
print(thistuple[-5:-2])
print(thistuple[:-5])
print(thistuple[-2:])

# Check if Item Exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Change Tuple Values, convert the tuple into a list, change the list, and convert the list back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# add an item, convert it into a list, add your item(s), and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Remove Item, Convert the tuple into a list, and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# delete the tuple completely
del thistuple

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# For loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)