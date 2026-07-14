from main20 import add
print(add(5,10))

# import entore function
import main20
print(main20.add(10,10))

# import function with alis
import main20 as ma
print(ma.add(10,15))

# libraries    below all
import random as rand
n=94654564564654
print(rand.randint(1,n))
print(rand.choice(["puni","dhanu"]))

# os library
# import os

# if not os.path.exists("data"):
#     os.mkdir("data")
#     for i in range(0,100):
#         os.mkdir(f"data/day{i+1}")

# high level operation of files 
import shutil
x=shutil.copy('source.txt','destination.txt')

# serialiazition 
import json
data={"name":"puneeth","age":21}

json_str=json.dumps(data)
print(json_str)
print(type(json_str))


#csv files 
import csv
with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['puneeth',21])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


#date time 
from datetime import datetime,timedelta
now=datetime.now()
print(now)

yestarday=now-timedelta(days=2)
print(yestarday)


# # file handling
# with open('source.txt','r') as file:
#     content=file.read()
#     print(content)
#     file.close()

# # read the file line by line 
# with open ("source.txt","r") as file:
#     for line in file:
#         print(line.strip())  #strip is used to remove the new line character


# read only one line
with open ("source.txt","r") as file:
    content=file.readlines()   #convert all lines into a single list 
    print(content)


# writing a file == the file exists it clear the old file and write fresh
with open ("source.txt","w") as file:
    file.write("puneeth\n")
    file.write("banglore\n")
    file.close()

# append == add a new content without deleting the o;d content
with open("source.txt","a") as file:
    file.write("chitradurga\n")
    file.write("banglore6464\n")
    file.close()

# writing the list of lines one by one
line=["shimoga\n","manglore\n"]
with open ("source.txt","a") as file:
    file.writelines(line)
    file.close()

# binary files read binary files
with open("binary.bin","rb") as file:
    content=file.read()
    print(content)

# read the content from source text file and write into the destination file 
with open ("source.txt","r") as file:
    content=file.read()
    
with open("puneeth.txt","w") as file:
    file.write(content)

# writing the file then reading

with open("source.txt","w+") as file:
    file.write("hello world\n")
    file.write("this is a new file\n")

    # move the file cursor to the begining
    file.seek(0)

    # read the content of the file
    content=file.read()
    print(content)


# working with file paths
# create a new directory

import os
new_directory="package1"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"directory {new_directory} created")
else:
    print(f"directory {new_directory} is already exists")


# list all the files and folders
items=os.listdir(".")
print(items)

word="hello"
with open("source.txt","r") as file:
    content=file.read()
    if word in content:
        print("found")
    else:
        print("not found")


