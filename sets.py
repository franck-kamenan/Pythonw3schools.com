thisset = {"apple", "banana", "cherry"}
print(thisset)

#Length
print(len(thisset))

# Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# 1 list can contain different data type
set4 = {"abc", 34, True, 40, "male"}
print(set4)

# type()
print(type(set4))

# The list() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# remove the last item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

# delete the set completely
del thisset

# empty the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# For loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# The intersection_update() method will keep only the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)