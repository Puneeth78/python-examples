
student={
    "name":"puneeth",
    "age":16,
     "grade":"A"
}
# iterate using for loop
for key in student.keys(): # same as value
    print(key)

# using get method
print(student.get("name"))
print("lat","key is not available") #using default value
print(student.values())
print(student.keys())
print(student["grade"])

student["age"]=17 #update the value
print(student)
student["address"]="india" #addd a new key
print(student)
del student["age"]   #delete the age
print(student)

# dictonary iteration
student={
    "name":"puneeth",
    "age":16,
     "grade":"A"
}
for key in student.keys():
    print(key)

for key in student.values():
    print(key)

for key,values in  student.items():
    print(key,values)


# nested dict
students={
   "student1":{"name":"puneeth","age":32},
   "student2":{"name":"dhanu","age":35}
}
print(students["student1"]["name"])

# iterate over nested dict
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")


# square number using for loop
dict={}
for i in range(0,6):
    dict[i]=i**2
print(dict)

# square using compherension
square={x:x**2 for x in range(11)}
print(square)

# conditional dict
# sqaure of even numbers 

square={x:x**2 for x in range(10) if x%2==0}
print(square)

# find the frequency of a list using dict
number=[1,2,3,4,5,5,6,6]
freq={}
for num in number:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)

# merge two dict into one using ** kwargs
dict1={"a":1,"b":2}
dict2={"c":9,"d":6}
merge_dict={**dict1,**dict2}
print(merge_dict)

# tuples revision
number=(1,2,3,4,5,6)
print(number[-1])

# tuple operations 
# concatination 
numbers=(1,2,3,4,5,6)
mixed_tuple=(1,2,3,"pp","l")
concatination=numbers+mixed_tuple
print(concatination)


# immutable nature of tuples
# meaning the elements cannot be changed once assign
num=(1,2,3,4,4,4,4,5,6)
# num[2]=10
print(num)

# methods .count()
print(num.count(4))

# find the index
print(num.index(4))   #return the first occurance of the element

# packed tuple 
packed_tuple=1,"hello",3.14
print(packed_tuple)


# unpcking tuple
a,b,c=packed_tuple
print(a)
print(b)
print(c)
print("end")
# unpacking tuple with star *
numbers=(1,2,3,5,6,4,5,6,4,6,54)
a,*b,c=numbers
print(a)
print(b)

# nested tupel and list
lst=[[1,2,3],["hello","puni"]]
print(lst[0][0:2])
print(lst[1][0])

# same as tuple as list
# iterate over nested tuple
tup=((1,2,3,4),("hello","puni","davanagere"))
for sub_tup in tup:
    for item in sub_tup:
        print(item,end=" ")
    print()


# create a to_do list example 1
to_do_list=["facewash","make tiffen","go to office"]

# adding the task
to_do_list.append("meeting in office")
to_do_list.append("got for a run")

# removing a completed task
to_do_list.remove("facewash")

# cheacking if a task in list
if "make tiffen" in to_do_list:
    print("dont forget to make the tiffen")

# remaining task
for task in to_do_list:
    print(f"reamining task - {task}")




# organising the student grade
grades=[85,96,85,63,5,2,85,99,45,23]

# append grade
grades.append(100)

# calculating the avg grade
avg_grade=sum(grades)/len(grades)
print(f"avg grade:{avg_grade:.2f}")

# finding tghe highest and lowest value
highest_grade=max(grades)
lowest_grade=min(grades)
print(f"highest_grade:{highest_grade}")
print(f"lowest_grade:{lowest_grade}")


# manage inventry
inventry=["apples","orange","banana"]

# add invenry
inventry.append("pomogranate")

# check if the item is stok
item="apples"
if item in inventry:
    print(f"yes {item }  is stok")
else:
    print(f"no {item} not available")

# printing the inventry list
print("inventry list")
for item in inventry:
    print(f"reamining item - {item}")


# collecting the user feedback
feedback=["great service","very satisfied","could be better","excellent experience"]

# adding new service
feedback.append("not happy with the service")

# counting the specefic feedback
positive_feedback=sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"positive feedback:{positive_feedback}")

# printing all fedback
print("user feedback")
for comment in feedback:
    print(f"- {comment}")


print("function is start---------------------11112223")


# functions
# organising code and reuseing code and improve readability
def even(n):
    if n%2==0:
        return "even"
    return  "odd"
       
print(even(5))

# function with multiple paramneter 
def add(a,b):
    return a+b
print(add(5,6))

# default parameter
def greet(name="puneeth"):
    print(f"hello {name}")
greet()

# variable length argumentts
# positional argument using *args
def print_number(*args):
    for i in args:
        print(i)
print_number(1,2,3,4,5,6,9,8,7,4,5,2)

# keyword argument *kwargs
def print_detail(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")
print_detail(name="puneeth",age=23,city="banglore")


# function examples
#  tempaturfe conversion
def convert_tempature(temp,unit):
    """this function converts celcius to faranate """
    if unit=="c":
        return temp*9/5+32 #cesius to f
    elif unit=="f":
        return (temp-32)*5/9
    else:
        return None
    
print(convert_tempature(25,"c"))
print(convert_tempature(77,"f"))

# password strength checker

def strong_password(password):
    if len(password)<8:
        return False
    elif not any(ch.isdigit() for ch in password):
        return False
    elif not any(ch.islower() for ch in password):
        return False
    elif not any(ch.isupper() for ch in password):
        return False
    elif not any(ch in "!@#$%^&*()" for ch in password):
        return False
    else:
        return True
password=input("enter the number: ")
print(strong_password(password))

# password is correct or not
password=1234
trial=0
while trial<3:
    input_pass=int(input(f"enter the password | {trial}: "))
    if password==input_pass:
        print("password is correct")
        break
    else:
        print("incorrect  try again")
        trial+=1

# calculate the total cost of the item
def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item["price"]*item["quantity"]
    return total_cost
cart=[
    {'name':'apple','price':100,'quantity':10},
    {'name':'banana','price':50,'quantity':10},
    {'name':'orange','price':80,'quantity':10},
    {'name':'pomogranate','price':60,'quantity':10}
]     

print(calculate_total_cost(cart))

# if the string is palindrome or not
def palindrome(name):
    if name==name[::-1]:
        return "True"
    else:
        return "false"
print(palindrome("malayalam i"))

# factorial of a number using rcursion
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
print(factorial(5))

# function read a file and count the frequency of the each word
def count_word_frequency(file_path):
    word_count={}
    with open(file_path,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('.,!@#$%^&*"|}{:"?><}')
                word_count[word]=word_count.get(word,0)+1
    return word_count
filepath='sample.txt'
word_frequency=count_word_frequency(filepath)
print(word_frequency)


arr=list(map(int,input("enter the number: ").split()))
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print(freq)

# lambda function
# the lambda function is ananymous function used to defined the function by using lambda keyword
result=lambda a,b:a+b
print(result(5,6))

# even number
even=lambda i:i%2==0
print(f"even {even(5)}")

# muyltiple parameter
addition=lambda a,b,c:a+b+c
print(f"addtion :{addition(5,5,5)}")

# map function
numbers=[1,2,3,6,5,4,7,8,9]
result=list(map(lambda x :x*x,numbers))
print(result)

# map multiple iterable
number1=[1,2,3]
number2=[4,5,6]
added_number =list(map(lambda number1,number2:number1+number2,number1,number2)) 
print(added_number)

# convert list of string into integer
str_number=['1','2','3','4','5']
int_number=list(map(int,str_number))
print(int_number)

str_num=["puneeth"]
result=list(map(str.upper,str_num))
print(result)

# filter
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)
print(list(result))

num=[1,2,3,6,5,4,8,9]
result=list(filter(lambda x:x%2==0,num))
print(result)

num=[1,2,3,4,5,6,7,8,9]
even_odd_greather_then_five=list(filter(lambda x:x>5 and x%2==0,num))
print(even_odd_greather_then_five)