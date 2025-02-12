# try:
#    You do your operations here
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.

# The try: block contains statements which are susceptible for exception

# If exception occurs, the program jumps to the except: block.

# If no exception in the try: block, the except: block is skipped.
# try:
#    You do your operations here
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.
# try:
#     print("hello")
# except :
#     print("world")
# else:
#     print("hero")

# try:
#    number = int(input("Enter a number: "))
#    result = 10 / number
#    print(f"Result: {result}")
# except ZeroDivisionError as e:
#    print("Error: Cannot divide by zero.")
# except ValueError as e:
#    print("Error: Invalid input. Please enter a valid number.")

# try:
#    # Code that might raise exceptions
# #    risky_code()
# finally:
#    # Code that always runs, regardless of exceptions
#    #cleanup_code()
#    x=4
#    print(x)

n = 5
for i in range(n):
    print('*' * n)
x=5
y=x
for i in range(x):
    for i in range(y):
        print("*",end="")
    print()
# OUTPUT :
# *****
# *****
# *****
# *****
# *****
x=5
for i in range(1,x+1):
    print(i*"*")
# OUTPUT:
# *
# **
# ***
# ****
# *****
x=5
for i in range(x,0,-1):
    print(i*"*")
# OUTPUT:
# *****
# ****
# ***
# **
# *
for i in range(1,x+5,2):
    print((i*"*").center(x+4))
# OUTPUT:
#     *
#    ***
#   *****
#  *******
# *********

#Diamond
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
x=5
for i in range(1,x*2,2):
    spaces=(x*2-i)//2
    print(" "*spaces + "*"*i)

x=5
for i in range(1,x*2,2):
    spaces=(x*2-i)//2
    print(" "*spaces + "*"*i)
for i in range(x*2-3,0,-2):
    spaces=(x*2-i)//2
    print(" "*spaces + "*"*i)
#to print the triangle both upright anda reverse then you have (or make diamond)
# for i in range(x*2-3,0,-2):
#     spaces=(x*2-i)//2
#     print(" "*spaces + "*"*i)

#Hollow Square
x=5
y=5
for i in range(y):
    if i==0 or i==y-1:
        print("*"*x)
    else:
        print("*"+" "*(x-2)+"*")

#Floyd's Triangle
# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
# 11 12 13 14 15  
n=5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
#Butterfly Pattern
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# x=5
# for i in range(1,x+1):
#     print("*"*i+" "*(9-2*i)+"*"*i)
x = 5
for i in range(1, x + 1):
    print("*" * i + " " * (2 * (x - i)) + "*" * i)
for i in range(n-1,0,-1):
    print("*" * i + " " * (2 * (x - i)) + "*" * i)

#Number Pyramid
#     1    
#    212   
#   32123  
#  4321234 
# 543212345
n = 5
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()




#Pascal Triangle
from math import comb

n = 5
for i in range(n):
    for j in range(i+1):
        print(comb(i, j), end=" ")
    print()
def pascal_triangle(n):
    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Sum of two above elements
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    return triangle

# Print Pascal’s Triangle for n rows
n = 5
for row in pascal_triangle(n):
    print(" ".join(map(str, row)))


#Hollow pyramid
# x=5
# for i in range(y):
#     if i==0 or i==y-1:
#         for i in range(1,5,4):


