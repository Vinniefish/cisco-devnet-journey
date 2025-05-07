# Single or double quotes
a = 'Hello'
b = "World"

# Triple quotes (for multiline strings)
c = '''This is
a multi-line
string.'''

print(a)
print(b)
print(c)

# String concatenation
greeting = a + ' ' + b
print(greeting)

# String repetition
laugh = 'ha' * 3
print(laugh)

#indexing
first_letter = a[0]
print(first_letter) # H

#negative indexing
last_letter = b[-1]
print(last_letter) # d

# Slicing. Slicing is inclusive of the start index and exclusive of the end index.
substring = a[0:5]  # up to but not including index 5
print(substring)  # Hello

"""
4. String Methods You MUST Know

Method	Purpose
lower()	Convert string to lowercase
upper()	Convert string to uppercase
strip()	Remove leading/trailing whitespace
replace(a, b)	Replace substring a with b
split(sep)	Split string by separator
join(list)	Join a list of strings

"""

# Case conversion
print(greeting.upper())
print(greeting.lower())

# Whitespace removal
dirty = "   messy text   "
print(dirty.strip())  # removes leading and trailing whitespace

# Replace
print(greeting.replace('World', 'Cisco'))  # replaces 'World' with 'Cisco

# Split
words = greeting.split(' ')  # splits string into a list of words
print(words)  # ['Hello', 'World']

# Join
rejoined = ' '.join(words)  # joins list of words into a string
print(rejoined)  # Hello World


"""" String Formatting (CRUCIAL for DevNet) 
When scripting with APIs or automating configurations, dynamic string building is very important."""

# 1. Old-style formatting (using % operator)

name = "Vincent"
print("Hello, %s!" % name)  # Hello, Vincent!

# str.format()

device = "Router1"
ip = "192.168.1.1"

print("Connecting to device {} at IP {}".format(device, ip))  # Connecting to device Router1 at IP

# f-strings (Python 3.6+)

username = "admin"
password = "cisco123"

print(f"Username: {username}, Password: {password}")  # Username: admin, Password: cisco123
# DevNet scripts prefer f-strings becuase they are more readable and efficient.


# Useful 'in' operator

message = "Welcome to Cisco DevNet!"
print("Cisco" in message)  # True
print("Python" in message)  # False

# Multiline String and Escaping Characters

multi = """Line 1
Line 2
Line 3"""
print(multi)

# Escape characters
example = "He said, \"Python is great!\""
print(example)  # He said, "Python is great!"
