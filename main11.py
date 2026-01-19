# Print numbers from 1 to 10
# Logic: Start from 1, stop at 10, increment each time
n=int(input("enter the number: "))
i=1
while i<=n:
    print(i)
    i+=1

# Print even numbers from 1 to 20
n=20
i=1
while i<=n:
    if i%2==0:
        print(i)
    i+=1

# # Print numbers in reverse (10 to 1)
# # Logic: Decrement instead of increment.
# i=10
while i>=1:
    print(i)
    i-=1

# Sum of first 10 natural numbers
i=1
total=0
while i<=10:
    total+=i
    i+=1
print("sum : ",total)

# Print multiplication table of a number
# Logic: Loop runs 10 times

n=5
i=1
while i<=10:
    print(f"{n}x{i}={n * i}")
    i+=1

# Count digits in a number
# Logic: Remove last digit using // 10.
number=1236589
count=0
while number!=0:
    count+=1
    number//=10
print("count: ",count)

# Reverse a number
# Logic: Extract last digit and rebuild number.

num=1234
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("reverse:",rev)

# Check whether a number is palindrome
# Logic: Reverse and compare.
num=121
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10

if rev==temp:
    print("palindrome")
else:
    print("not palindrome")

# Find factorial of a number
# Logic: Multiply repeatedly
num=5
fact=1
while  num>0:
    fact*=num
    num-=1
print(fact)

# Keep taking input until user enters 0
# Logic: Sentinel value loop (very common in interviews).
num = int(input("Enter a number: "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number: "))

print("Loop ended")

# Let’s stop counting sheep after 5 sheep, even though the condition allows counting up to 10:
sheep_count=1
while sheep_count<=10:
    print(f"sheep count:{sheep_count}")
    if sheep_count==5:
        print("count is enough")
        break
    sheep_count+=1
print("exit loop")

# Let’s say you want to skip counting sheep that are number 4:
sheep_count=1
while sheep_count<10:
    sheep_count+=1
    if sheep_count==4:
     continue
    print(f"sheep count:{sheep_count}")
print("exit loop")

# et’s ask the user for a PIN until they enter the correct one:
pin=1234
while True:
    input_pin=int(input("enter the pin: "))
    if input_pin==pin:
        print("enter pin in valid")
        break
    else:
        print("inncorrect pin try again")

# Write a Python program to check a user’s PIN with a maximum of 3 attempts using a while loop.
pin=1234
trials=0
while trials<3:
    input_pin=int(input(f" trail {trials} | enter the pin : "))
    trials+=1
    if pin==input_pin:
         print("correct")    
         break
    else:
        print("incorrect try again")
print("three time completed ")

# Simulate a snack vending machine where a user can continue buying snacks only while the machine has snacks available and the user has sufficient money, using appropriate loop and condition logic.
available_snack=4
money=10
while available_snack>0 and money > 0:
    print(f"available snaks:{available_snack} | money : {money}")
    buy=input("you want buy a snack with money 5₹ (yes/no):")
    if buy=="yes":
           print("snack purchased")
           available_snack-=1
           money-=5
           
    else:
          print("not purchased")
print("snack sold out or you not have money")

# Print odd numbers from 1 to 50.
num=0
while num<=50:
    print(num)
    num+=2

# Take a number from the user and print numbers from 1 to that number.
n=int(input("enter the number: "))
num=1
while num<=n:
    print(num)
    num+=1

# # Ask the user for a number and print its digits one by one. in reverse order 
number=int(input("enter the number: "))
while number>0:
    print(number)
    number+=1
    
 # Ask the user for a number and print its digits one by one. in same order
number=int(input("enter the number: "))
rev=0
temp=number
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10

while rev>0:
    digit=rev%10
    print(digit)
    rev//=10

# Count how many digits are in a given number (without using len).
number=1234
count=0
while number!=0:
    count+=1
    number//=10
print(count)

# Find the sum of digits of a number.
num=1234
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
print(sum)

# Find the product of digits of a number
number=1234
product=1
while number>0:
    digit=number%10
    product*=digit
    number//=10
print(product)


# Check whether a number is an Armstrong number  using while loop
num=int(input("enter the number: "))
temp=num
count=0
while temp>0:
    count+=1
    temp//=10

temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**count
    temp//=10

if sum==num:
    print("armstromg")
else:
    print("not armstrong")

