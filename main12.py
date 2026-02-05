# # Print numbers from 1 to 5
for i in range(1,6):
    print(i)

# # Print even numbers from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i) 

# # Print characters of a string
name="python"
for ch in name:
    print(ch)
   
# # Sum of numbers from 1 to 5
sum=0
for i in range(1,6):
    sum+=i
print(sum)

# # Print multiplication table of a number
num=5
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

# # Print multiplication table 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
      
# # Count digits in a number
num=1234
count=0
for i in str(num):
    count+=1
print("digits:",count)

# # Find factorial of a number
num=5
fact=1
for i in range(1,num+1):
    fact*=i
print("factorial num :",fact)

# #  Find sum of digits of a number
num=123
sum_digits=0
for i in str(num):
    sum_digits+=int(i)
print(sum_digits)

# # Check whether a number is even or odd (1 to 5)
for i in range(1,6):
    if i%2==0:
        print("even")
    else:
        print("odd")

# # Write a program that counts how many vowels are in a given string using a for loop
string="davanagere"
vowels="AEIOUaeiou"
for ch in string:
    if ch in vowels:
        print(ch)

# # Find the product of digits of a number
digit=1234
product=1
for i in str(digit):
    product*=int(i)
print(product)


# # Reverse a string using a for loop.
string="python"
rev=""
for ch in string:
    rev=ch+rev
print(f"the reverse of {string} : ",rev)

# Find the largest number in a list.
list=[20,89,50,63,56]
largest=list[0]
for num in list:
    if num>largest:
        largest=num
print("largest num: ",largest)

# Print common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
for i in list1:
    if i in list2:
        print(i)



# enumarate function in python
list=["puneeth","chitradurga","davanagere","banglore"]
for index,ch in enumerate(list):
    print(index,ch)


tup=("1","puneeth","5","davanagere","banglore")
for index,ch in enumerate(tup):
    print(index,ch)

string=["puneeth","dhanush","kannada","english","davanagere"]
for index,ch in enumerate(string,start=1):
    if index==3:
        continue
    else:
        print(index,ch)

# shortend if else
age=18
result="eligable for vote"  if age>18 else "not eligable" 
print(result)

password=1234
correct_pin=int(input("enter the password: "))
result="correct pin" if correct_pin==password else "incorrect pin"
print(result)

# looping throw lists
# sum of all lists
numbers=[1,2,3,4,5,6]
sum=0
for i in numbers:
    sum+=i
print("total sum is : ",sum)

# doubling each number into a string
list=[1,2,3,4,5,6]
double=[]
for num in list:
    double.append(num*2)
    print(double)
print("double number is : ",double)


# looping throw dic
student_marks={"puneeth":85,"puni":56,"puneeth V":96}
for name,marks in student_marks.items():
    if name=="puni":
        break
    print(f"{name} : {marks}")

# for loop with range
students=["puneeth","puni","punee"]
marks=[98,96,89]
student_marks={}
for index,student in enumerate(students):
    student_marks[student]=marks[index]
print(student_marks)

# or
students=["puneeth","puni","punee","dhanush"]
marks=[98,96,89,93]
student_marks={}
for i in range(0,len(students),2):
    student_marks[students[i]]=marks[i]
print(student_marks)

# list comprehension
l=[1,2,3,4,5,6]
new_list=[x for x in l]
print(new_list)

lst=[x for x in range(0,101)]
new_list=[x for x in lst if x%2==0]
print(new_list)

str=["puneeth","dhanush","pueeth"]
cs=[x[2] for x in str ]
print(cs)

name="python"
result=[x for x in name if x in "aeiou"]
print(result)


n=2
# print(type(n))
x=(n)
print(x,sep="-")

