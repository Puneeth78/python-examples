# # 1) Write a Python program to find out what version of Python you are using.
import sys
print("python version")
print(sys.version)
print("varsion info.")
print(sys.version_info)

# #  2) Write a Python program to display the current date and time.
import datetime

# # Get the current date and time
now = datetime.datetime.now()

# # Print formatted date and time
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# # Circle Area Calculator
import math
r=1.1
pi=3.80
circle=math.pi*(r**2)
print(circle)

# # Print first and last name in reverse order with a space between them
first=input("enter the name: ")
last=input("enter the name: ")
print(f"{last}  {first} ")

# # Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
data=input("enter the number: ")
list_num=data.split(",")
tuple_num=tuple(list_num)
list_num=list(data)
tuple_num=tuple(data)
print("list:",list_num)
print("tuple: ",tuple_num)

# # # Write a Python program that accepts a filename from the user and prints the extension of the file
filename=input("input the file name: ")
f_extns=filename.split(".")
print(f"the extension of the file is:" + repr(f_extns[-1]))

# # Write a Python program to display the first and last colors from the following list.
color_list=["red","while","blue","green"]
ans=color_list[0],color_list[3]
print(ans)

# # # Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date=(11,12,2014)
print(f"the exam will be start from : {exam_st_date[0]}/ {exam_st_date[1]}/ {exam_st_date[2]}")


# # # Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
a = input("Input an integer: ")   # keep as string first
# Create n1, n2, n3 by concatenating the string and then type cast to int
n1 = int(a)
n2 = int(a + a)
n3 = int(a + a + a)
# Add all three numbers
print(n1 + n2 + n3)

# # built in functions
# # Write a Python program to print the documents
# Print the docstring (documentation) of the 'abs' function
print(abs.__doc__) #return the absolute value
print(len.__doc__) #stored function
print(sum.__doc__) #sum
print(map.__doc__) # docstring (documentation) of the 'map' function
print(filter.__doc__) #docstring (documentation) of the 'filter' function

# # print calender 
import calendar
y=int(input("enter the year: "))
# m=int(input("enter the month: "))
print(calendar.calendar(y)) 


# # Write a script that takes a date and prints the weekday name.
year=int(input("enter the year: "))
month=int(input("enter the month: "))
day=int(input("enter the day: "))
date=datetime.date(year,month,day)
print("the day of the week is:",date.strftime("%A")) #,strfime("%A") returns the full weekday(like monday tuesday etc)


# # Days Between Dates

# # Write a Python program to calculate the number of days between two dates.
from datetime import date
f_date=date(2006,3,15)
l_date=date(2006,3,17)
result=l_date - f_date
print("the difference between two dates is :",result.days)

# # rite a Python program to get the volume of a sphere with radius six.
import math
r=6
v=4/3*math.pi*(r**3)
print("the volume of the sphere  is: ",v)

# # 1. Surface Area of a Sphere  Area=4πr2
import math
r = float(input("Enter the radius of the sphere: "))
area = 4 * math.pi * (r ** 2)
print("The surface area of the sphere is:", area)

# # 2. Volume of a Cylinder
import math
r=float(input("enter the radius of the cylinder: "))
h=float(input("enter the height of the cylinder: "))
volume=math.pi*(r**2)*h
print("the volume of the cylinder is: ",volume)

#  Get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
def difference(n):
    if n>=17:
        return abs(n-17)
    else:
        return (n-17)*2
print(difference(22))
print(difference(17))

# or

n=int(input("enter the number:  "))
if n>=17:
    result=abs(n-17)*2
else:
    result=17-n
print(result)
