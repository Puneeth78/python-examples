# find the factorial numbers in python
# the factorial number is product of all positive numbers 

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

# Using a Recursive Approach
def factorial(n):
    if n==0 or n==1:
     return 1
    else:
       return n*factorial(n-1)
factorial(5)
print(factorial(5))

# by using ternary opearation
def fact(n):
   return 1 if(n==0 or n==1) else n* fact(n-1)
num=5
print(fact(num))

# using math
import math
def factorial(n):
 return(math.factorial(n))
mum=6
print(factorial(num))

# Using numpy.prod()
# This Python code calculates the factorial of n using NumPy. It creates a list of numbers from 1 to n, computes their product with numpy.prod(), and prints the result.
import numpy
n=5
x=numpy.prod([i for i in range(1,n+1)])
print(x)

# sum using numpy
import numpy as np
number=[1,2,3,6,5,4]
x=np.sum(number)
print(x)

# multiply all elements
import numpy as np
number=[1,2,3,4,5]
x=np.prod(number)
print(x)

# find the mean of the number
import numpy as np
number=[1,2,3,4]
x=np.mean(number)
print(x)

# FIND THE SIMPLE INTEREST
#  Simple Interest = (P x T x R)/100
# Using function i write a example
def fun(p,t,r):
   return(p*t*r)/100
p,t,r=8,6,8
res=fun(p,t,r)
print(res)

# Using lambda function
si=lambda p,t,r:(p*t*r)/100
p,t,r=5,6,4
res=si(p,t,r)
print(res)

# Using list comprehension
p,t,r=8,9,6
res=[p*t*r/100][0]
print(res)

# function examples
def fun():
   print("welcome to CFG")

# Calling a Function
def fun():
   print("helo world")
fun()


# Function Arguments
# Syntax:
# def function_name(parameters):
#     """Docstring"""
#     # body of the function
#     return expression

# We will create a simple function in Python to check whether the number passed as an argument to the function is even or odd.
def evenOdd(num):
   if num%2==0:
      return "even"
   else:
      return "odd"
print(evenOdd(5))
print(evenOdd(10))

# Types of Function Arguments

# 1. Default Arguments
# A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
def fun(x,y=10):
   print("x:",x)
   print("y:",y)
fun(5)


def name(n1,n2="dhanush"):
   print("n1:",n1)
   print("n2:",n2)
n1="puneeth"
print(name(n1))

# 2. Keyword Arguments
# In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.

def student(fname,lname):
   print(fname,lname)
student(fname="puneeth",lname="rajkumar")
student(lname="rajkumar",fname="puneeth")
      
# 3. Positional Arguments
# In positional arguments, values are assigned to parameters based on their order in the function call.
def student(name,age):
   print(f"my name is {name}")
   print(f"i am {age} years old")
print("case=1:")
print(student("puneeth",20))

print("case-2")
print(student("dhanush",15))

# add two numbers
def add(a,b):
   print(f"the sum is : {a + b}")
print(add(10,5))

# 4. Arbitrary Arguments
# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
def fun(*args,**kwargs):
   print("non-keyword argument (*args):")
   for arg in args:
      print(arg)

   print("key word argument (**kwargs)")
   for key,value in kwargs.items():
      print(f"{key} == {value}")

fun("hey","hi",first="kannada",second="english")
