import re
#Check if the string starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

# The findall() Function
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # Return a list containing every occurrence of "ai"

import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt) # Check if "Portugal" is in the string
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# The search() Function
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# The split() Function
import re
txt = "The rain in Spain"
x = re.split("\s", txt) # Split the string at every white-space character
print(x)

import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1) # Split the string at the first white-space character
print(x)

# The sub() Function
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt) # Replace all white-space characters with the digit "9"
print(x)

import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # Replace the first two occurrences of a white-space character with the digit 9
print(x)

# Match Object
import re
txt = "The rain in Spain"
x = re.search("ai", txt) # The search() function returns a Match object
print(x)

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # Search for an upper case "S" character in the beginning of a word, and print its position
print(x.span())

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # The string property returns the search string
print(x.string)

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # Search for an upper case "S" character in the beginning of a word, and print the word
print(x.group())