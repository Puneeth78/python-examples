name="puneeth"
print(type(name))


a=10
a+=10
a-=10 
a=a-10
a=10
a**=10   #a=a*10
print(a)

print(True or False)
print(True and False)
print(True and True)
print(not(True))

x=5
y=6
print(not(y>x))

list=[1,2,3,4]
print(1 in list)
print(5 in  list)



string="12"
num=2
string_num=int(string)
sum=string_num+num
print(sum)
print(type(sum))

p=10
string_p=str(p)
print(string_p)
print(type(string_p))

a=10.1
b=10
a_int=int(a)
# sum=a+b
print(type(sum))

name=input("enter the name: ")
print(f"hi good morning {name } how are you")


num=int(input("enter the number"))
square=num*num
print(f"entered {num} of square is = {square}")

a=int(input("enter the number a : "))
b=int(input("enter the number b : "))
c= a+b 
print(f" the sum of {a} + {b} is {c}")
age=int(input("enter the age : "))
if age > 18:
    print("eligable of vote")
else:
    print("not eligable for vote")

string=input("enter the string: ")
print(f" the length of the string is {len(string)} ")

price=int(input("enter the price: "))
quantity=int(input("enter the qunatity: "))
total_cost=price*quantity
print("the total cost is : ",total_cost)

number=int(input("enter the number: "))
if number%2==0:
    print("even")
else:
    print("odd")

a=int(input("enter the number a: "))
b=int(input("enter the number b: "))
c=int(input("enter the number c: "))
if a>=b and a>=c:
    print(f"{a} is largest")
elif b >=c and b>=c:
    print(f"{b} is greather ")
else:
    print(f"{c} is grearther")

print("largest number is : ",max(a,b,c))

string=input("enter the string: ")
if string==string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

num=int(input("enter the multiplicaation number : "))
for i in range (1,11):
    print(f"{num} X {i}={num * i}")

radius=int(input("enter the radius : "))
area = 3.14 * (radius*radius)
print(area)

a=15
b=4
print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>b))

string=input("enter the string: ")
if "python" in string:
    print("yes")
else:
    print("no")

sentence=input("enter the string: ")
word=sentence.split()
print(word)

first_name="puneeth"
last_name="anjana"
full_name= first_name + " " + last_name
print(full_name * 10)
name=" !!! puneeth !!! "
print(name[0])
print(name[5])
print(name[1:6])
print(name[:5])
print(name[1:])
print(name[-1])
print(name[-7])
print(name[:-1])
print(name[-4:-1])
print(name[::2])
print(name[0:6:2])
print(name.upper())
print(name.strip(" ! "))
message="warning puneeth1"
print(message.replace("warning","error"))
print(message.capitalize())
print(message.split())
print(message.count("e"))
print(message.center(50))
print(message.endswith("h"))
print(message.find("anju")) 
print(message.index("p"))
print(message.isalpha())
print(message.isalnum())
print(message.islower())
print(message.isupper())
print(message.istitle())
print(message.startswith("W"))
print(message.title())
print(message.swapcase())

name=input("enter the name: ")
age=int(input("enter the age: "))
print(f"hello {name}! you are a {age} years old")

sentence=input("enter the name: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","_"))