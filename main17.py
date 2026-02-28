def add(a,b):
    return a+b
print(add(5,5))

def greet():
    print("puneeth")
greet()

def fun(x,n):
    if n==0:
        return
    print(x)
    fun(x,n-1)
fun(15,4)

def fun(x,n):
    if x>n:
        return
    print(x)
    fun(x-1,n)
fun(1,5)

def fun(x, n):
    if x > n:
        return

    print("Forward:", x)   # Step 1 (Do work)

    fun(x+1, n)            # Step 2 (Recursive call)

    print("Backtrack:", x) # Step 3 (Undo / Coming back)

fun(1, 5)

def fun(sum,i,n):
    if i>n:
        print(sum)
        return
    fun(sum+i,i+1,n)
fun(0,1,10)

def func(n):
    
    if n==1:
        return 1
    return n+func(n-1)
print(func(5))

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def reverse_array(arr, start, end):
    # Base case
    if start >= end:
        return
    
    # Swap first and last elements
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursive call on the remaining subarray
    reverse_array(arr, start + 1, end - 1)

# Example
arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr) - 1)
print(arr)


def fun(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return fun(s,left+1,right-1)
s="nitin"
print(fun(s,0,len(s)-1))

nums=[6,3,5,2,1]
nums.sort(reverse=True)
print(nums)

print(type(1/1))


def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[5,7,8,4,1,6,9,2]
print(selection_sort(arr))
    

x=5;y=5;z=x+y
print(z)

age=20
age_str=str(age)
# print(age_str)
print(type(age_str))

age='20'
print(type(int(age)))

height=5.11
print(int(height))
print(float(int(height)))

var=10
print(var,type(var))

var="puni"
print(var,type(var))

a="puni"
b="puni"
print(a!=b)

num=int(input("enter the number: "))
if num>=0:
    print("num is positive")
    if num%2==0:
        print("num is even")
    else:
        print("num is odd")
print("num is negative")

year=int(input("enter the year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not a leap year")

num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
operator=input("enter the operator +,-,*,/,//,% : ")

if operator=="+":
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    if num2!=0:
       result=num1/num2
    else:
        print("zero division error")
else:
    print("enter the wrong operator")  

print("result",result)     


age=int(input("enter the age: "))
is_student=input("are you a student ot not (yes/no): ")
if age<5:
    print("ticket free")
elif age<=12:
    print("pay 15rs")
elif age >=18:
    if is_student=="yes":
        print("pay 20rs")
    else:
        print("pay 25rs")
elif age<=30:
    if is_student=="yes":
        print("pay 45rs")
    else:
        print("pay 60rs")

else:
    print("you enter wrong details")

count=0
while count<=5:
    
    print(count)
    count+=1

color=["green","pink","yellow","red"]
for i in color:
    for j in i:
        print(f"i:{i} and j:{j}")

i=1
total=0
while i<=10:
    total+=i
    i+=1
print(total)


sum=0
for i in range(0,11):
    sum+=i
print(sum)

for num in range(1,10):
    if num>1:
        for i in range(2,num):
            if num%i==0:
               break
        else:
            print(f"{num}")

fruits=["orange","apple","orange","banana"]
length=[len(word) for word in fruits]
print(length)
for index,fruit in enumerate(fruits):
    print(index,fruit)
fruits[2]="pomogranate"
fruits.insert(0,"berry")
fruits.append("pinaple")
fruits.remove("apple")
index=fruits.index("orange")
print(index)
print(fruits.count("orange"))
# print(fruits.index("watermilon"))
print(fruits)
# print(fruits[0])
print(fruits[-3:-1])

number=[ "even" if x %2==0 else "odd" for x in range(0,11) ]
print(number)

list1=[1,2,3,4]
list2=['a','s','d','f']
pair=[[i,j]for i in list1 for j in list2]


my_set={1,2,3,4,5,6,7,8}
lst=my_set.pop()
print(lst)
# my_set.add(10)
# my_set.remove(8)
print(my_set)
# print(type(my_set))

set1={1,3,4,5,10,3,6,7,8 ,10,2}
set2={1,10,4,2,3,6,5,7,8}

# issubset
s3=set1.issubset(set2)
print(s3)

# is supper set
s4=set1.issuperset(set2)
print(s4)
# union
print(set1.union(set2))

# intersecxtion
print(set1.intersection(set2))

# symmetirc_differenced
print(set1.symmetric_difference(set2))

# difference
print(set1.difference(set2))

lst=[1,2,3,2,3,6,5,6,4,5,6,5,8,9,8]
print(set(lst))

text="puneeth is the good in is  boy in davanafere"
words=text.split()
print(words)
print(set(words))





