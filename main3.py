# Find Maximum of two numbers in Python
a=7
b=3
print(max(a,b))

# using ternary operator
x=10
y=20
res=x if x>y  else y
print(res)

# using if else statement
p=15
q=20
if p>q:
    print(p)
else:
    print(q)

# by using sort()
s=10
t=45
num=[s,t]
num.sort()
print(num[1])

#  Finding the Maximum of 3 Integer Variables
g=10
h=20
i=30
max_value=max(g,h,i)
print(f"the max value among three varibles is : {max_value}")

#  Finding the Maximum of 3 String Variables
var1="puneeth"
var2="dhanush"
var3="rocking star"
max_str=max(var1,var2,var3)
print(f"the max valustring among three varibles is : {max_str}")

# Python max() Exception
# a="puneeth"
# b=25
# max_value=max(a,b)
# print(max_value)  #out put is type error because it not supported between str and int

# Python max() Index
def max_positions(a):
    maxpos=a.index(max(a)) + 1
    print("the maximum is at position : ",maxpos+1)
a=[3,2,1,4,5,6]
max_positions(a)


# Ternary Operator
# even or odd
n=5
res="even" if n%2==0 else "odd"
print(res)

# nested if else
n=-5
res="positive" if n>0 else "negative" if n<0 else "zero"
print(res)

# Nested (3-way) decision, e.g., grading:
score = 85
grade = "A" if score >= 90 else "B" if score >= 75 else "C"
print(grade)  # → "B"

# Ternary Operator using Tuple
n=7
res=("even","odd")[n%2!=0]
print(res)

# Pass/Fail based on score(tuple)
score=85
res=("faiil","pass")[score>=35]
print(res)

# Adult/Minor based on age(tuple)
age=18
res=("not eligable for vote","eligable for vote")[age>18]
print(res)

# Ternary Operator using Dictionary
a=10
b=20
res={True:a,False:b}[a<b]
print(res)

# Ternary Operator with Print Function
age=18
print("eligable for vote"  if age>18 else  "not eligable for vote")

# Ternary Operator using Python Lambda
time=8
res=(lambda time:"breakfast" if time>=8 else "no breakfast")(time)
print(res)
