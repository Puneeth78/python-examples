# a=int(input("enter a: "))
# b=int(input("enter b: "))
# try:
#     print(a/b)
# except Exception as e:
#     print(f"error is came :{e}")
#     b=int(input("enter b:"))
#     print(a/b)
# else:
#     print("here is no error")
# finally:
#     print("program is ended  ! if error is occurs or not i am not care")


# try:
#     num=int(input("enter the number: "))
#     result=10/num
#     print("result :",result)
# except ZeroDivisionError:
#     print("you entered zero")
# except ValueError:
#     print("you entered string")

# num=int(input("enter the number: "))
# if num<0:
#     raise ValueError("negative number are not alloted")
# else:
#     print("you enterd number: ",num + 10)


# age=int(input("enter the age: "))
# try:
#     if age<100:
#      print(f"he will take {100-age} years to become 100 old")
#     else:
#      raise ValueError("age is alredy 100")
# except Exception as e:
#     print(f"  more than 100 value cause error {e}")

# finally:
#     print("the program is close")

# age = int(input("enter the age: "))

# try:
#     if age < 100:
#         print(f"he will take {100-age} years to become 100 old")
#     else:
#         raise ValueError("Age is already 100 or more")

# except Exception as e:
#     print(f"More than 100 value caused error: {e}")

# finally:
#     print("the program is close")

# # short end if else
# age=int(input("enter the age: "))
# x= "eligable for vote" if  age>18 else "not eligable got vote"
# print(x)



# try:
#     a=b
# except NameError as e:
#     print(e)

# try:
#     a=int(input(""))
#     b=int(input(""))
#     c=a/b
# except ZeroDivisionError as zero:
#     print(zero)
# else:
#     print(int(c))



# try:
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     c=a/b
# except ZeroDivisionError as zero:
#     print(zero)

# except Exception as e:
#     print(e)

# else:
#     print(c)


# try:
#     num=int(input("enter the num:"))
#     result=10/num
# except ValueError:
#     print("enter the valid number")
# except ZeroDivisionError:
#     print("enter the number above zero")

# age=int(input("enter the age:"))
# try:
#     if age>18:
#         print("eligable for vote")
#     else:
#      raise ValueError("enter the number above 18")
   
# except Exception as e:
#     print(e)
   
# file handling and exception handling
try:
    file=open("example.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("the file not found ")

finally:
    print("file is not found in the library")


