#Arrays
# An array is a container which can hold a fix number of items and these items should be of the same type. Each item stored in an array is called an element and they can be of any type including integers, floats, strings, etc.
# SYNTAX
# importing 
# import array as array_name

# # creating array
# obj = array_name.array(typecode[, initializer])
import array as parth
he=parth.array('f',[3,4,6,7])
print(he)
print(type(he),he)
print(he[0])
he.insert(4,67)#first index dalo then joh number enter  karana hai
print(he)
he.remove(3)# Number dalo joh delete karana hai 
print(he)
#search karega ki element hai ya nhi fir uska index return karega
print(he.index(7))
he[2]=32
print(he)
#accessing element using iteration
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# iteration through for loop
for item in numericArray:
   print(item)

#enumerate() function
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# use of enumerate() function
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")

#accessing a range of index
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# slicing operation
print (numericArray[2:])
print (numericArray[0:3])

#Append() Method
import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)

#Insert Method insert(i, v) i is index and v is value
a.insert(1,20)
print (a)

#extend() Function can ad two array
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)

#Remove Array Item array.remove(v) or array.pop(i)in this index fill karna padta hai
a.remove(10)
print(a)
a.pop(1)
print(a)

#reversing array
a.reverse()
print(a)

#Sort an Array
a=list(a)
a.sort()
print(a)

#Exercise
#1. Print Largest Number in Array
import array as test
a=test.array('i',[22,54,72,43,65,23])
largest=a[0]
for i in a:
    if i > largest:
        largest= i
print(largest)

#OR 
print(max(a))

#2. Python program to store all even numbers from an array in another array
b=arr.array('i')  #Creating a new array for even number
for i in a:
    if i%2==0:
        b.append(i)
print(b.tolist())# for simble b it will convert it to b but to convert b.tolist() then it will convert it to list


#Python program to find the average of all numbers in a Python array
import array as b
a=b.array('i',[2,43,3,5,54])
d=len(a)
print(b)
total=0
for i in a:
    total+=i
print(total/d)
