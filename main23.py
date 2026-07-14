# # sum of natural numners
# numbers=5
# sum=0
# for i in range(0,numbers+1):
#     sum+=i*2
    
# print(sum)

# # num=int(input("enter the number:"))

# # if num%2==0:
# #     print(f"{num} is even")
# # else:
# #     print(f"{num} id odd")

# # num=int(input("enter the numner:"))
# # if num<=1:
# #     print("num is not prime")
# # if num==2:
# #     print("num is not prime")
# # if num%2==0:
# #     print("num is not prime")
# # else:
# #     print("num is prime")

# # print  perfect vaklid square
# num=3
# i=1
# while i*i<=num:
#     if i*i==num:
#         print("valid square")
#         break
#     i+=1
# else:
#     print("not valid")


# num = int(input("Enter a decimal number: "))

# binary = bin(num)[2:]

# print("Binary:", binary)

# n=5
# binary=""
# while n>0:
#     remainder=n%2
#     binary=str(remainder)+binary
#     n//=2

# print("number : " ,binary)

# import math
# num1=10
# num2=12

# gcd=math.gcd(num1,num2)
# print("gcd: ",gcd)

s="puneeth"
unique=''
for ch in s:
    if  ch not in unique:
        unique+=ch
print(unique)

p="puneethisagoodboy"
vowels="AEIOUaeiou"
total_count=0
for ch in p:
    if ch not in vowels:
        total_count+=1
print("total count:",total_count)


a='cat'
b='bat'
if len(a)==len(b):
    if sorted(a)==sorted(b):
        print("srting is anagram")
    else:
        print("string is not anagram")


s = "note"
t = "trne"

if len(s) != len(t):
    print("not anagram")
else:  

    char_count_s = [0] * 26
    char_count_t = [0] * 26

    for char in s:
        char_count_s[ord(char) - ord('a')] += 1

    for char in t:
        char_count_t[ord(char) - ord('a')] += 1

    flag=True

    for i in range(26):
        if char_count_s[i] != char_count_t[i]:
            flag=False

    if flag:
        print("anagram")
    else:
        print("not anagram")



print('hello world')