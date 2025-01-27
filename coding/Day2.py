<<<<<<< HEAD
#loops
=======
x=str("Parth")
x=int(10.0)
x=float(20.5)
x=complex(4+5j)
x=list((5,3,2))
print(x)
x=tuple((2,3,342,23))
print(x)
x=set((1,2,3))
print(x)
for i in range(25,100,5): #range(start, stop, step)
   print(i,end=" ")          #The end parameter in print() allows you to specify what should be added after the printed value. By default, it's "\n", but you can change it to something else, like a space, a comma, or even an empty string.

num=[]
for i in range(25,100,5):
    num.append(i)
print(num)

x=dict(name="parth",age=23)
print(x)
x=frozenset(("apple","camera"))
print(x)
import random
print(random.randrange(1,19))
#string length
a=" kya haal hai"
print(len(a))
#check string
print("hai"in a)
#slicing
print(a[:5])
#UPPERCASE
print(a.upper())
#lowercase
print(a.lower())
#removing White Space
print(a.strip())
#Replace string
print(a.replace('k','a'))
#Split String
print(a.split())# if you pt split(something) then it will split where that charater is present
#format
age=20
z="adss"
new=("my age is {1} {0}")
print(new.format(age,z))
#Small Practice
# z=str(input("enter Your Name:"))
# x=int(input("Enter Your Age:"))
# y=str(input("tell about yourself"))
# u="Your Name is {} and Your age is {}\n your hobby is {}"
# print(u.format(z,x,y))

#Apppend
x=[20,30,4,3]#not work with tuple ,Works with  List
x.append(50)
print(x)
>>>>>>> bc07228 (day3)

#Insert()
x.insert(2,34)
print(x)
# #Extend
# y=[32,43,54]
# x.extend(y)
# print(x)
#Remove
x.remove(20)
print(x)
#Remove Specified Index Use pop()
x.pop(1)
print(x)
#Remove Last Index
x.pop()
print(x)
#Use Del
del x[2]
print(x)
#or
# del()
#Clear
# x.clear()
# print(x)


#Loop Through index Number
list=[2,43,23,34,12]
for i in range(len(list)):
    print(list[i],end=" ")

#using while loop
i=0
while i<len(list):
    print(list[i])
    i+=1
#List Comprehension
# newlist=[i for i in list if '20' in i]
# print(newlist)

#Sort
list.sort()
print(list)
#in descending
list.sort(reverse=True)
print(list)

#customize sort Function
x=[23,76,54,67,256]
def myfunc(n):
    return abs(n-50)
x.sort(key=myfunc)
print(x)

#Reverse
x.reverse()
print(x)

#Copy
p=x.copy()
print(p)

























