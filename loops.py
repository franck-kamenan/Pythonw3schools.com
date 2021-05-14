# The while Loop
i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

# The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:  # Note that number 3 is missing in the result
    continue
  print(i)

# The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
for x in "banana":
  print(x)

# The break Statement in For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue Statement in For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() Function
for x in range(6):
  print(x)

# adding a parameter
for x in range(2, 6):
  print(x)

# specify the increment value by adding a third parameter
for x in range(2, 30, 3):
  print(x)

# Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break # If the loop breaks, the else block is not executed.
  print(x)
else:
  print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement in For Loop
for x in [0, 1, 2]:
  pass # having an empty for loop like this, would raise an error without the pass statement