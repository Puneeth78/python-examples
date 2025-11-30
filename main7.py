# # even or odd number using def function
def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

num=int(input("enter the number: "))
even_odd(num)
print(even_odd)

# # max of two number
a=[10,20,30]
print(max(a))

# # # read two number 
a=int(input("enter the number a: "))
b=int(input("enter the number b: "))
sum=a+b
print("sum=",sum)
if sum==30:
    print("print sum is 30")
else:
    print("print num is not 30")

# # largest three number
a=10
b=30
c=25
if a>c and b>c:
    print(f" {a} a  is largest")
elif b>c:
    print(f" {b} b is largest")
else:
    print(f"{c} c is largest")

# # # cheak positive negative or zero
num=int(input("enter the number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")

# # # sum of n natural number using for loop
num=int(input("enter the numbner: "))
sum=0
for i in range(1,num+1):
    sum+=i
print(f"the sum of {num} is : {sum}")

# fibonacci logic building
num=int(input("enter an integer : "))
if num<=1:
    print(f"entered {num} is not prime")
else:
    for i in range(2,num):
          if num%i==0:
               print(f"{num} is not prime")
               print(f"{i} is the factor of {num}")
               break
    else:
        print(f"enter num {num} is prime")


# # fibonacci sequence 
terms=int(input("enter the terms: "))
n1,n2=0,1
if terms<=1:
    print("please enter the positive integers")
elif terms==1:
    print(f"fibonacci sequence:{n1}")
else:
    for term in range(terms):
        print(n1,end=" ")
        n=n1+n2
        n1=n2
        n2=n

def fib(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter a non-negative integer: "))
print(f"Fibonacci number F({n}) = {fib(n)}")






    
