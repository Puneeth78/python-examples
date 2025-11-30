
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















