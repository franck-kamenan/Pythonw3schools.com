thislist = ["apple", "banana", "cherry"]
print(thislist)

#Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Length
print(len(thislist))

# Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# 1 list can contain different data type
list4 = ["abc", 34, True, 40, "male"]
print(list4)

# type()
print(type(list4))

# The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[0])

# Negative Indexing
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:5])
print(thislist[2:])
print(thislist[-5:-2])
print(thislist[:-5])
print(thislist[-2:])

# Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[0] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# insert more items than you replace
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#insert less items than you replace
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# insert a new list item, without replacing any of the existing values
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert a list item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "orange")
print(thislist)

# append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)

thatlist = ["apple", "banana", "cherry"]
del thatlist[0]
print(thatlist)

# remove the last item
thislist.pop()
print(thislist)

# delete the list completely
del thatlist

# empty the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# For loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
thislist = ["apple", "papaya", "orange"]
[print(x) for x in thislist]

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thatlist = [100, 50, 65, 82, 23]
thatlist.sort()
print(thatlist)
thislist.sort(reverse = True)
thatlist.sort(reverse = True)
print(thislist)
print(thatlist)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Sensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)