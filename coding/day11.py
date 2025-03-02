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
n = int(input("Enter the number: "))

if n < 2:
    print("Non Prime")  # 0 and 1 are not prime
else:
    for i in range(2, int(n ** 0.5) + 1):  # Because every non-prime number has at least one factor ≤ √n.
        if n % i == 0:
            print("Non Prime")
            break
    else:
        print("Prime")


#3
n=int(input("enter the number"))
fact=1
for i in range(n,1,-1):
    fact=fact*i
print(fact)

#4
n=input("enter")
rev=''
for i in range(len(n)-1,-1,-1):
    rev=rev+n[i]

print(rev)


#5
n=input("enter the number")
a=list(n)
sum=0
for i in range(len(a)):
    sum=sum+int(a[i])
print(sum)

