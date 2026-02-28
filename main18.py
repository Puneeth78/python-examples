
student={
    "name":"puneeth",
    "age":16,
     "grade":"A"
}
# iterate using for loop
for key in student.keys(): # same as value
    print(key)

# using get method
print(student.get("name"))
print("lat","key is not available") #using default value
print(student.values())
print(student.keys())
print(student["grade"])

student["age"]=17 #update the value
print(student)
student["address"]="india" #addd a new key
print(student)
del student["age"]   #delete the age
print(student)

# dictonary iteration
student={
    "name":"puneeth",
    "age":16,
     "grade":"A"
}
for key in student.keys():
    print(key)

for key in student.values():
    print(key)

for key,values in  student.items():
    print(key,values)


# nested dict
students={
   "student1":{"name":"puneeth","age":32},
   "student2":{"name":"dhanu","age":35}
}
print(students["student1"]["name"])

# iterate over nested dict
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")


# square number using for loop
dict={}
for i in range(0,6):
    dict[i]=i**2
print(dict)

# square using compherension
square={x:x**2 for x in range(11)}
print(square)

# conditional dict
# sqaure of even numbers 

square={x:x**2 for x in range(10) if x%2==0}
print(square)

# find the frequency of a list using dict
number=[1,2,3,4,5,5,6,6]
freq={}
for num in number:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)

# merge two dict into one using ** kwargs
dict1={"a":1,"b":2}
dict2={"c":9,"d":6}
merge_dict={**dict1,**dict2}
print(merge_dict)