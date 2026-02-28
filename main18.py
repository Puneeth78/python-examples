
# student={
#     "name":"puneeth",
#     "age":16,
#      "grade":"A"
# }
# # iterate using for loop
# for key in student.keys(): # same as value
#     print(key)

# # using get method
# print(student.get("name"))
# print("lat","key is not available") #using default value
# print(student.values())
# print(student.keys())
# print(student["grade"])

# student["age"]=17 #update the value
# print(student)
# student["address"]="india" #addd a new key
# print(student)
# del student["age"]   #delete the age
# print(student)

# # dictonary iteration
# student={
#     "name":"puneeth",
#     "age":16,
#      "grade":"A"
# }
# for key in student.keys():
#     print(key)

# for key in student.values():
#     print(key)

# for key,values in  student.items():
#     print(key,values)


# # nested dict
# students={
#    "student1":{"name":"puneeth","age":32},
#    "student2":{"name":"dhanu","age":35}
# }
# print(students["student1"]["name"])

# # iterate over nested dict
# for student_id,student_info in students.items():
#     print(f"{student_id}:{student_info}")
#     for key,value in student_info.items():
#         print(f"{key}:{value}")


# # square number using for loop
# dict={}
# for i in range(0,6):
#     dict[i]=i**2
# print(dict)

# # square using compherension
# square={x:x**2 for x in range(11)}
# print(square)

# # conditional dict
# # sqaure of even numbers 

# square={x:x**2 for x in range(10) if x%2==0}
# print(square)

# # find the frequency of a list using dict
# number=[1,2,3,4,5,5,6,6]
# freq={}
# for num in number:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1
# print(freq)

# # merge two dict into one using ** kwargs
# dict1={"a":1,"b":2}
# dict2={"c":9,"d":6}
# merge_dict={**dict1,**dict2}
# print(merge_dict)

# tuples revision
number=(1,2,3,4,5,6)
print(number[-1])

# tuple operations 
# concatination 
numbers=(1,2,3,4,5,6)
mixed_tuple=(1,2,3,"pp","l")
concatination=numbers+mixed_tuple
print(concatination)


# immutable nature of tuples
# meaning the elements cannot be changed once assign
num=(1,2,3,4,4,4,4,5,6)
# num[2]=10
print(num)

# methods .count()
print(num.count(4))

# find the index
print(num.index(4))   #return the first occurance of the element

# packed tuple 
packed_tuple=1,"hello",3.14
print(packed_tuple)


# unpcking tuple
a,b,c=packed_tuple
print(a)
print(b)
print(c)
print("end")
# unpacking tuple with star *
numbers=(1,2,3,5,6,4,5,6,4,6,54)
a,*b,c=numbers
print(a)
print(b)

# nested tupel and list
lst=[[1,2,3],["hello","puni"]]
print(lst[0][0:2])
print(lst[1][0])

# same as tuple as list
# iterate over nested tuple
tup=((1,2,3,4),("hello","puni","davanagere"))
for sub_tup in tup:
    for item in sub_tup:
        print(item,end=" ")
    print()


# create a to_do list example 1
to_do_list=["facewash","make tiffen","go to office"]

# adding the task
to_do_list.append("meeting in office")
to_do_list.append("got for a run")

# removing a completed task
to_do_list.remove("facewash")

# cheacking if a task in list
if "make tiffen" in to_do_list:
    print("dont forget to make the tiffen")

# remaining task
for task in to_do_list:
    print(f"reamining task - {task}")




# organising the student grade
grades=[85,96,85,63,5,2,85,99,45,23]

# append grade
grades.append(100)

# calculating the avg grade
avg_grade=sum(grades)/len(grades)
print(f"avg grade:{avg_grade:.2f}")

# finding tghe highest and lowest value
highest_grade=max(grades)
lowest_grade=min(grades)
print(f"highest_grade:{highest_grade}")
print(f"lowest_grade:{lowest_grade}")


# manage inventry
inventry=["apples","orange","banana"]

# add invenry
inventry.append("pomogranate")

# check if the item is stok
item="apples"
if item in inventry:
    print(f"yes {item }  is stok")
else:
    print(f"no {item} not available")

# printing the inventry list
print("inventry list")
for item in inventry:
    print(f"reamining item - {item}")


# collecting the user feedback
feedback=["great service","very satisfied","could be better","excellent experience"]

# adding new service
feedback.append("not happy with the service")

# counting the specefic feedback
positive_feedback=sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"positive feedback:{positive_feedback}")

# printing all fedback
print("user feedback")
for comment in feedback:
    print(f"- {comment}")