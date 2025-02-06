#and Operator
a=200
b=20
c=23
if b<a and b<c:
    print("hurray")

#OR Operator
if a>b or a>c:
    print("hurray")
else:
    print(3)

#Nested Statement
x=41
if x>10:
    if x==10:
        print(2)
    else:
        print(3)

a=33
b=23
if b==a:
    pass

#while Loop
i=1
while i<7:
    print(i)
    i+=1

#the continue Statement
i=0
while i<2:
    print(i)
    i+=1
else:
    print("Khatam")

#python Function
# def function_name( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]
# call by value − When a variable is passed to a function while calling, the value of actual arguments is copied to the variables representing the formal arguments. Thus, any changes in formal arguments does not get reflected in the actual argument. This way of passing variable is known as call by value.

# call by reference − In this way of passing variable, a reference to the object in memory is passed. Both the formal arguments and the actual arguments (variables in the calling code) refer to the same object. Hence, any changes in formal arguments does get reflected in the actual argument.
def callme(n):
    print(n)
callme(4)

def testfunction(arg):
   print ("ID inside the function:", id(arg))

var = "Hello"
print ("ID before passing:", id(var))
testfunction(var)

def add(x,y):
   z=x+y
   return z
a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))

#Arbitary argument 
def my_func(*args):
    total=sum(args)
    print(total)
my_func(2,42,23,34)

#Arbitary Keywords argument
def my_func(*kwargs):
    print(kwargs)
my_func("hello","bhai","kya haal hai")

#PAssing a list
def my_func(n):
    for i in n:
        print(i)
my_func([5,2,3,4,5,])

#Return Values
def my_func(x):
    return 5*x
print(my_func(20))

#Lambda Function
#syntax lambda argument :expression
x=lambda a:a+10
print(x(5))

#lambda function can even take multiple argument
x=lambda a,b :a**b
print(x(5,3))

#class Object
class myclass:
    x=5
print(myclass)

#create object
class myclass:
    x=5
p1=myclass()
print(p1)

#the _init function
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("parth",20)
print(p1.name,p1.age)

#Object Method
class Person:
    def __init__(parth,name,age):
        parth.name=name
        parth.age=age
    def my_func(age):
        print("my name is")
p1=person("",)

        