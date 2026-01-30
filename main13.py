# # function examples 
# def greet():
#     print("hello,welcome to python!")
# greet()

# # function with one argument
# def greet(name):
#     print("hello",name)
# greet("puni")

# # function with multiple argument
# def add(a,b):
#     print(a+b)
# add(5,6)

# # function with return value
# def multiply(a,b):
#     return a*b
# result=multiply(6,5)
# print(result)

# # name with default argument
# def greet(name="friend"):
#     print("hello",name)
# greet()

# # check even or odd
# def even_odd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# print(even_odd(5))

# # function using a list
# def total_marks(marks):
#     return sum(marks)
# marks=[20,20,20,20,20]
# print(total_marks(marks))

# # multiple argument 
# def rectangle(length,width):
#     return length * width
# print(rectangle(5,6))

# # keyword argument
# def greet(name,age=21,city="cta"):
#     print(f"name={name} age={age} city={city}")
# greet("puneeth")

# # required argument 
# def town(nam):
#     print(nam)
# town("jsdh")

# args
# add multiple numbers
def add_numbers(*args):
    total=0
    for num in args:
        total+=num
    return total
# add_numbers=int(input("enter the numbers: "))
print(add_numbers(1,2,3,4))

# find maximum numbers
def find_max(*args):
    return max(args)
print(find_max(2,5,8,9,6,5))

# count argument
def count(*args):
    return len(args)
print(count(1,2,3,6,5,8,9))


# *args with normal argument
def student(name,*marks):
    print("name: ",name)
    print("marks: ",marks)
student("puni",85,90,78)

# *args in a loop
def print_items(*items):
    for item in items:
        print(item)
print_items("apple","bannana","mango")

# Passing list to *args
def add_numbers(*args):
    return sum(args)
nums=[10,20,30]
print(add_numbers(*nums))

# *args with default argument
def calculate(base,*nums):
    total=base
    for n in nums:
        total+=n
    return total
print(calculate(10,2,65))

def shopping_bill(*args):
    return sum(args)

print(shopping_bill(100, 250, 80))

# Print key–value pairs using kwargs
def student_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
student_details(name="puneeth",cgpa=7.22,collage="vtu")

# Basic if–else with **kwargs
def check_login(**kwargs):
    if kwargs.get("username")=="admin" and kwargs.get("password")=="1234":
        print("login sucessfull")
    else:
        print("invalid input")

check_login(username="admin",password="1234")

# def check_login(**kwargs):
#     if kwargs.get("username") == "admin" and kwargs.get("password") == "1234":
#         print("Login successful")
#     else:
#         print("Invalid credentials")

# check_login(username="admin", password="1234")

def check_email(**kwargs):
    if "email" in kwargs:
        print("Email:",kwargs["email"])
    else:
        print("Email not provided")

check_email(name="Puni",email="puni@.1234")

# If–elif–else using **kwargs
def ticket_price(**kwargs):
    age=kwargs.get("age")

    if age is None:
        print("age is not provided")
    elif age>5:
        print("provide half ticket")
    elif age<60:
        print("provide sinior ticket")
    else:
        print("full ticket")
ticket_price(age=20)
