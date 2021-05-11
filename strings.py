# Single or double quotes
print("Hello")
print('Hello')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings with three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# Strings Arrays
a = "Hello, World!"
print(a[0])

# For loop
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)
print("free" not in txt)

# If statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

# Slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))
print(a.capitalize())
print(a.casefold())
print(a.title())

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# With index numbers
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))