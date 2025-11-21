
# # examples using *args
def add_numbers(*args):
   total=0
   for num in args:
      total+=num
   print("sum:",total)
add_numbers(2,3,5)


# # using kwargs
def student_info(**kwargs):
   for key,value in kwargs.items():
      print(f"{key} : {value}")
student_info(name="puneeth",age=21,place="banglore")

# # using both args and kwargs
def details(*args,**kwargs):
   print("positional argument (*args )")
   for i in args:
      print(i)

   print("keyword argument (**kwargs)")
   for key,value in kwargs.items():
      print(f"{key}:{value}")

details("laptop","mouse",brand="asus vivobook",price=500000,gen="15")

print("2" * 3 + "1")

# Python Program for Compound Interest
P=float(input("enter the principle amount: "))
R=float(input("enter the annual interest rate: "))
T=float(input("enter the time in years : "))
A=P*(1+ R/100)** T  # A= the amount after T years(principle + interest)
CI=A-P  #CI=compound interest earned A-P
print("compound interest: ",CI)

# Using Built-in pow() Function
p=1000
r=10.25
t=5
amt=p*(pow((1+r/100),t))
CI=amt-p
print("compound interest: ",CI)

# Using for Loop
# In this example, we use a for loop to calculate compound interest by repeated multiplications.
p=1200
r=5.5
t=2
amt=p
for i in range(t):
    amt=amt*(1+r/100)
CI=amt-p
print("compound interest:",CI)

# Python For Loops
s=["puneeth","dhanush"]
for i in s:
    print(i)

# Python For Loop with String
s="puneeth"
for i in s:
    print(i)

# Using range() with For Loop
for i in range(0,11):
    print(i)

# 1)
for i in range(0,11):
    print(i,end=" ")
print()

# We are using the range function in which we are passing the starting and stopping points with the jump of the iterator.
for i in range(0,10,2):
    print(i,end=" ")
print()

# If a user wants to increment, then the user needs steps to be a positive number.
for i in range(4,44,4):
    print(i,end=" | ")
print()

# If a user wants to decrement, then the user needs steps to be a negative number. 
for i in range(40,0,-4):
    print(i,end=" | ")
print()

