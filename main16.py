# python basics
l=["puneeth"]
print(type(l))
print(l[-1][-6:-3])
print(l[-1][:-4])
print(l[:2])
print(l[0:2])
print(l[0:])
print(l[:6])

l=["p","u","n","e","t","h"]
print(l[0])
print(l[:2])
print(l[3:])
print(l[-6:-1])
print(l[::-1])
print(tuple(l[-6:-1]))
print(len(l))

l=["p","u","n","e","t","h"]
for i in range(0,len(l)):
    # print(l[i])
    print(l[i])

a=[1,2,3,4]
total=0
for i in range(len(a)):
    total+=a[i]
print("sum : " ,total)

a=[1,2,4,3]
a.sort(reverse=True)
print(a)

number=[1,5,2,3]
largest=number[0]
for num in number:
    if num>largest:
        largest=num
print(f"largets element :  {largest}")

nums=[2,7,11,15]
target=9
num_container={}
for index,num in enumerate(nums):
    complement=target-num
    if complement in num_container:
       print(num_container[complement],index)
    num_container[num]=index
M=int(input())
a=set(map(int,input().split(",")))


N=int(input())
b=set(map(int,input().split(",")))
print(a)
print(b)

l=["puneeth"]
print(l[0][3])
print(l[-1][-1])
print(l[-1][::-1])


arr=[1,8,100,56,90]
largest=arr[0]
for i in arr:
    if i > largest:
        largest=i
print("largest number: ",largest)

def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = ""
        
#         for i in range(len(strs[0])):
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return res
#             res += strs[0][i]   # ✅ moved outside inner loop
            
#         return res 


A=[1,2,3,4,5,6]
#  0 1 2 3 4 5
print(A[2])
A[4]=8
print(A)
A.append(5)
print(A)


import array
arr = array.array('i', [10, 20, 30])
arr.append(40)   # ✅ works
print(arr)

n=10
for i in range(1,n+1):
    print("puneeth")
    

import math
def count_digit(n):
    return 

num=121
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if rev==num:
    print("palindrome")
else:
    print("not palindrome")

num=153
temp=num
count=len(str(num))
total=0
while temp>0:
    digit=temp%10
    total=total+digit**count
    temp//=10
if num==total:
    print("strong")
else:
    print("no strong")

import math
num=36
for i in range(1,num+1):
    sqrt=math.sqrt(i)
    print(f"sqrt of {i}:{sqrt}")


num=[4,5,3,1,2]
num.sort()
print(num)
print(num[-2])

n=30
print(n//2)

arr=[1,2,3,5]
n=len(arr)+1
accepted_ouput=n*(n+1)//2
actual_output=sum(arr)
missing=accepted_ouput-actual_output
print(f"the missing element is:{missing}")

n = 36

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# print num is prime or not
num=int(input("enter the number: "))
if num<=1:
    print("num is not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("num is not prime")
            break
    else:
         print("num is a prime")

# hashing
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num<0 or num>10:
        print("zero")
    else:
        print(hash_list[num])

# for alphabet
s="azyxyyzaaaa"
q=["d","a","y","x"]
hash_list=[0]*26
for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list[index]+=1
for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(hash_list[index])

def greet():
    print("hello")
    greet()
greet()

def print_name(n):
    if n==0:
        return
    print("puneeth")
    print_name(n-1)
print_name(4)

