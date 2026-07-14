# # n=12345
# # count=0
# # while n>0:
# #     n=n//10
# #     count+=1
# # print(f"the number of digits in the number is: {count}")

# # n=12345
# # temp=n
# # rev=0
# # while temp>0:
# #     digit=temp%10
# #     rev=rev*10+digit
# #     temp//=10
# # print(f"the reverse of {n} is: {rev}")

# # n=122
# # temp=n
# # rev=0
# # while temp>0:
# #     digit=temp%10
# #     rev=rev*10+digit
# #     temp//=10

# # if n==rev:
# #     print(f"{n} is a palindrome")
# # else:
# #     print(f"{n} is not a palindrome")

# n=153
# temp=n
# sum=0
# count=len(str(n))
# while temp>0:
#     digit=temp%10
#     sum=sum+(digit**count)
#     temp//=10
# if n==sum:
#     print(f"{n} is an armstrong number")
# else:    
#     print(f"{n} is not an armstrong number")


# n=10
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# num=int(input("enter the number: "))
# if num<1:
#     print("the num is not prime")
# else:
#     if num==2:
#         print("the num is prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("the num is not prime")
#                 break
#         else:
#             print("the num is prime")

# def funNum(num):
#     print(num)
#     if(num==1):
#         return 1
#     funNum(num-1)

# funNum(5)

# def power2(num):
#     if num==0:
#         return 1
#     elif num==1:
#         return 2
#     else:
#         return 2*power2(num-1)
# print(power2(5))

# def fibonaci(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fibonaci(num-1) + fibonaci(num-2)
# print(fibonaci(5))


arr=[1,3,4,5]
# if len(arr)==0 or len(arr)==1:
#     print("arr is sorted")
# else:
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             print("arr is not sorted")
#             break
#     else:
#         print("arr is sorted")

# def isSorted(arr):
#     if len(arr)==0 or len(arr)==1:
#         return True
#     ans=isSorted(arr[1:])
#     if arr[0]<arr[1]:
#         return ans
#     else:
#         return False
# print(isSorted(arr))


def count_frequency(arr,n):
    freq={}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]]=1
    return freq




arr=[1,2,2,3,1,4,5]
n=len(arr)
result=count_frequency(arr,n)
print(result)
