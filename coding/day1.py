#Python is a very popular general-purpose interpreted, interactive, object-oriented, and high-level programming language. Python is dynamically-typed and garbage-collected programming language.
#Python is Interpreted − Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to PERL and PHP.
#Python is Object-Oriented − Python supports Object-Oriented style or technique of programming that encapsulates code within objects.
#Python is a Beginner's Language − Python is a great language for the beginner-level programmers and supports the development of a wide range of applications from simple text processing to WWW browsers to games.
#Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.

# Python is Interpreted − Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to PERL and PHP.

# Python is Interactive − You can actually sit at a Python prompt and interact with the interpreter directly to write your programs.

# Python is Object-Oriented − Python supports Object-Oriented style or technique of programming that encapsulates code within objects.

# Python is a Beginner's Language − Python is a great language for the beginner-level programmers and supports the development of a wide range of applications from simple text processing to WWW browsers to games.

# 2. Line-by-Line Execution
# Python processes and executes one line of code at a time.
# If there's an error in one line, the execution stops at that point, and the interpreter shows an error message.
# Dynamic Typing
# Python uses dynamic typing, meaning you don't need to declare variable types explicitly. The interpreter figures out the type during execution:
# python
# Copy
# Edit
# x = 10       # Python recognizes this as an integer
# x = "Hello"  # Now it recognizes this as a string
#import this
print("Hello, World!")
x=20
y=30
print(x+y)
# Deleting Multiple Variable at a time
del x,y
#print(x) ,print(y)#this will Create an Error
# CASTING IN Python
x=str(10)#This Will Be '10'
X=int(10)#This will be 10
z=float(10)#This Will be 10.0
print(x) ,print(X) ,print(z)
print(type(x))
print(type(X))
print(type(z))

#Python Variable : Multiple Assignment
x=y=z=10
x,y,z=10,20,30
x,y,z=10,20,'Hello'

#Python Variables - Naming Convention
#Every Python variable should have a unique name like a, b, c. A variable name can be meaningful like color, age, name etc. There are certain rules which should be taken care while naming a Python variable:

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number or any special character like $, (, * % etc.
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Python variable names are case-sensitive which means Name and NAME are two different variables in Python.
#Python reserved keywords cannot be used naming the variable.

#Python Local Variable
def sumy(x,y): #My point in you can make any function Not Means 'sum' only
    sumy=x+y
    return sumy
print(sumy(6,9))#This are local variable thar means that are use in this only and not anywhere

#Python Global Variable
x=2
y=3
def addi(x,y):
    addi=x+y
    return addi
print(addi(x,y))

#Alternative
x=2
y=3
def addi():
    addi=x+y
    return addi
print(addi())

# Types of Data Types in Python
# Python supports the following built-in data types −

# Numeric Data Types
# int
# flot
# complex
# String Data Types
# Sequence Data Types
# list
# tuple
# range
# Binary Data Types
# bytes
# bytearray
# memoryview
# Dictionary Data Type
# Set Data Type
# set
# frozenset
# Boolean Data Type
# None Type

#Numeric Data Type
Var1=10
Var2=10.1
Var3=1e+2j
Var4=True
print(type(Var1))
print(type(Var2))
print(type(Var3))
print(type(Var4))

#String(Python string is a sequence of one or more Unicode characters, enclosed in single, double or triple quotation marks)
#string[start:stop:step]

x="Parth Bhardwaj"
print(x)  # Prints complete string
print(x[0]) # Prints first character of the string
print(x[2:5]) # Prints characters starting from 3rd to 5th
print(x[:-5])
print(x[-1:-5])#Empty String because step is positive that ir goes to left to right
print(x[-1:-5:-1])
print(type(x))
print( x*2) # Prints string two times
print(x+' Hero')# Prints concatenated string

# 3. Python Sequence Data Types
# List Data Type-A Python list contains items separated by commas and enclosed within square brackets ([])
# Tuple Data Type- Python tuple consists of a number of values separated by commas and enclosed with parentheses
# Range Data Type-A Python range is an immutable sequence of numbers which is typically used to iterate through a specific number of items.

#List
#Nested List[[10,20,20],[30,20,19],[30,34,56]]
x=[20,20,30,'john','hero','balveer']
y=[23]
print(x)
print(type(x))
print(x[2:5])
print(x[:5])
print(x[:-5])
print(x[-1:-5])
print(x[-1:-5:-2])
print(x+y)#concatenated list

#Tuple 
#Nested Tuple(['One', 'Two', 'Three'], 1,2.0,3, (1.0, 2.0, 3.0))
x=(20,20,30,'john','hero','balveer')
y=(23,)# comma is very Important
print(x)
print(type(x))
print(x[2:5])
print(x[:5])
print(x[:-5])
print(x[-1:-5])
print(x[-1:-5:-2])
print(x+y) #concatenated list

#Range
#range(start, stop, step)
for i in range(5):
    print(i)
for i in range(1,5,3):
    print(i)
#Python Binary Data Types
#A binary data type in Python is a way to represent data as a series of binary digits, which are 0's and 1's
#bytes
# bytearray
# memoryview

# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)

# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value) 
# using memory view
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)
x=b'28'
y=memoryview(x)
print(y)

#Dictionary View
#Python dictionary is like associative arrays or hashes found in Perl and consist of key:value pairs. The pairs are separated by comma and put inside curly brackets {}
E={1:'hello',2:'hero',3:'mujhe shakti do'}
print(x)
print(type(x))
x={}
z={23}
print(x)
print(y)
print(z)
print(E[2])

