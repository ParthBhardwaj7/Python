# Questions
# 1️⃣ Print the first N Fibonacci numbers using a loop.
# 2️⃣ Check if a number is prime using a loop.
# 3️⃣ Find the factorial of a number using a loop.
# 4️⃣ Reverse a given number (e.g., input 1234, output 4321).
# 5️⃣ Print the sum of digits of a number (e.g., 123 → 1+2+3=6).
n=int(input("Enter no"))
a,b=0,1
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)
#OR
n = int(input("Enter N: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#2






