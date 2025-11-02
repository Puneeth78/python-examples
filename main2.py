#  1) add two numbers
a=60
b=48
res=a+b
print(f"the sum of a + b is : {res}")

# taking input from the user
a=int(input("enter the number  a: "))
b=int(input("enter the number b: "))
res=float(a) + float(b)
print(f"the sum is : {res}")

# using function
def add(a,b):
    return a + b
a=10
b=20
res=a+b
print(res)

# using lambda function
res=lambda a,b:a + b
print(res(10,2))

res=lambda a,b:a//b
print(res(8,3))

# using operator
import operator
print(operator.add(2,2))

import operator
print(operator.sub(10,2))

# using sum
print(sum([10,5]))

# 2) minimum of two numbers
a=7
b=6
print(min(a,b))

# using conditional statements
a=10
b=15
if b<a:
    print(f"the min is{b}")
else:
    print(f"the min is : {a}")

# using ternary operation (short hand)
a=10
b=25
res=a if a<b else b
print(res)

# even or odd
num=int(input("enter the number : "))
result= "even" if num % 2==0 else "odd"
print(result)

# Check Positive or Negative
num=-3
result="positive" if num>0 else "negative"
print(result)

# Using with Strings
user="puneeth"
result="welcome puneeth!" if user == "puneeth" else "here is no puneeth"
print(result)


# Python Program to Find the Gcd of Two Numbers
a=60
b=48
while b!=0:
    remainder=a%b
    a=b
    b=remainder
print(a,"is the gcd")

# Using math.gcd()
import math
a=60
b=48
print(math.gcd(a,b))

# Using subtraction based gcd
a=60
b=48
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a

# # Python program to add two binary numbers.
a="1101"
b="100"
sum=bin(int(a,2)) +bin(int(b,2))
print(sum[2:]) 

# Method: Using "add" operator 
from operator import*
num1="1101" 
num2="100" 
print(bin(add(int(num1,2),int(num2,2))))
