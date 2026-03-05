
# logic building program
# sum of natural numbners
n=int(input("enter the number: "))
sum=0
while n>0:
    sum+=n
    n-=1
print(sum)

# reverse number
num=int(input("enter the number: "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print(f"the reverse of {num} is :",rev)

# cheak the num is even or odd 
number=int(input("enter the number: "))
i=number
while i==number:
    if i%2==0:
        print("enter number is evevn")
    else:
        print("enter the number is odd")
    break


# merge sort
def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i +=1 
        else:
            merged.append(list2[j])
            j += 1

    # Add remaining elements
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


list1 = [1,3,5]
list2 = [1,2,4,6]

print(merge_sorted_lists(list1, list2))


# # rotate a list

num=[1,2,3,4,5,6,7]
# nums=[num[-1]]+num[0:6]
# print(nums)
n=len(num)
temp=num[n-1]
for i in range(n-2,-1,-1):
    num[i+1]=num[i]
num[0]=temp
print(num)

# brute force solution for rotate
num=[1,2,3,4,5,6,7]
k=2
for i in range(0,k):
    e=num.pop()
    num.insert(0,e)
print(num)






