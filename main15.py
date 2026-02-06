a=int(input("enter a: "))
b=int(input("enter b: "))
try:
    print(a/b)
except Exception as e:
    print(f"error is came :{e}")
    b=int(input("enter b:"))
    print(a/b)
else:
    print("here is no error")
finally:
    print("program is ended  ! if error is occurs or not i am not care")


try:
    num=int(input("enter the number: "))
    result=10/num
    print("result :",result)
except ZeroDivisionError:
    print("you entered zero")
except ValueError:
    print("you entered string")

num=int(input("enter the number: "))
if num<0:
    raise ValueError("negative number are not alloted")
else:
    print("you enterd number: ",num + 10)


age=int(input("enter the age: "))
try:
    if age<100:
     print(f"he will take {100-age} years to become 100 old")
    else:
     raise ValueError("age is alredy 100")
except Exception as e:
    print(f"  more than 100 value cause error {e}")

finally:
    print("the program is close")

age = int(input("enter the age: "))

try:
    if age < 100:
        print(f"he will take {100-age} years to become 100 old")
    else:
        raise ValueError("Age is already 100 or more")

except Exception as e:
    print(f"More than 100 value caused error: {e}")

finally:
    print("the program is close")

# short end if else
age=int(input("enter the age: "))
x= "eligable for vote" if  age>18 else "not eligable got vote"
print(x)

