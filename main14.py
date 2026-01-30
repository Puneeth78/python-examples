def add(a,b):
    print(a+b)
add(5,5)

# Write a function to find the square of a number.
def square(num):
    return num*2
print(square(2))

# Write a function that checks whether a number is even or odd.
def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(8))

# Write a function that returns the maximum of two numbers.
def max_num(numbers):
    return max(numbers)
print(max_num([2,3,5,6]))

# Write a function to calculate the area of a circle.
def area_circle(radius):
    return 3.142*radius*radius
print(area_circle(5))

# Write a function that takes a name and prints a greeting message.
def greet(name):
    print(f"{name} hello ")
greet("puneeth")

# Write a function to find the factorial of a number.
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
print(factorial(5))

# or
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))

# Write a function that counts the number of vowels in a string.
def vowels(string):
    count=0
    for ch in string:
        if ch in "aeiou":
            count+=1
    return count
string=input("enter the word: ")
print(vowels(string))

# Write a function to reverse a string.
def reverse(string):
    rev=""
    for ch in string:
        rev=ch+rev
    return rev
string=input("enter the string: ")
print(reverse(string))

# Write a function that checks whether a number is prime.
def prime_num(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if i%n==0:
             return False
        return True
print(prime_num(7))


n=int(input("enter the number: "))
if n<=1:
    print("num is not prime")
else:
    for i in range(2,n):
        if i%n==0:
            print("not prime")
        else:
            print("prime")




