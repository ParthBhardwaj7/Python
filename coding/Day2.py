#Python Arithmetic Operators
# +	Addition	a + b = 30
# -	Subtraction	a – b = -10
# *	Multiplication	a * b = 200
# /	Division	b / a = 2
# %	Modulus	b % a = 0
# **	Exponent	a**b =10**20
# //	Floor Division	9//2 = 4

#Python Comparison Operators
# Operator	Name	Example
# ==	Equal	(a == b) is not true.
# !=	Not equal	(a != b) is true.
# >	Greater than	(a > b) is not true.
# <	Less than	(a < b) is true.
# >=	Greater than or equal to	(a >= b) is not true.
# <=	Less than or equal to	(a <= b) is true.

#Python Assignment Operators
# Operator	Example	Same As
# =	a = 10	a = 10
# +=	a += 30	a = a + 30
# -=	a -= 15	a = a - 15
# *=	a *= 10	a = a * 10
# /=	a /= 5	a = a / 5
# %=	a %= 5	a = a % 5
# **=	a **= 4	a = a ** 4
# //=	a //= 5	a = a // 5
# &=	a &= 5	a = a & 5
# |=	a |= 5	a = a | 5
# ^=	a ^= 5	a = a ^ 5
# >>=	a >>= 5	a = a >> 5
# <<=	a <<= 5	a = a << 5

# Python Bitwise Operators
# Operator	Name	Example
# &	AND	a & b
# |	OR	a | b
# ^	XOR	a ^ b
# ~	NOT	~a
# <<	Zero fill left shift	a << 3
# >>	Signed right shift	a >> 3

# Python Logical Operators
# Operator	Name	Example
# and	AND	a and b
# or	OR	a or b
# not	NOT	not(a)

# Python Membership Operators
# Operator	Description	Example
# in	Returns True if it finds a variable in the specified sequence, false otherwise.	a in b
# not in	returns True if it does not finds a variable in the specified sequence and false otherwise.	a not in b

#Python Identity Operators
# Operator	Description	Example
# is	Returns True if both variables are the same object and false otherwise.	a is b
# is not	Returns True if both variables are not the same object and false otherwise.	a is not b

#Python User Input
#The input () Function
#The raw_input () Function
'''e=input("enter the number")
Class=input("enter the number")
print(name)
print("This Is Code For Length Breadth")
length =int(input("enter Length"))
Width=int(input("enter Width"))
Area=length*Width
print("area is",Area)'''

#if Statements
marks = 80
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"
print(result)


#The match Statement

def vowel(n):
    match n:
        case 'a': return 'vowel hai'
        case _: return 'galt bola'
print(vowel('b'))
print(vowel('a'))
































