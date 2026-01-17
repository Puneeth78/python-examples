# # # Write a Python program to print vowels along with their index positions.
name="puneeth"
vowels="aeiou"
for i in range(len(name)):
    if name[i] in vowels:
        print( name[i]," at index " ,i)

# # # Write a Python program to check whether a string contains at least one vowel or not.
name="puneeth"
vowels="aeiou"
for i in range(len(name)):
    if name[i] in vowels:
        print( name[i]," at index " ,i)
        break

# # # Replace all spaces in a string with -
sentence=input("enter the sentence: ")
print(sentence.replace(" ","_"))

# # reverse a string
name="puneeth"
print(name[::-1])

# # Print each character of a string on a new line
a="venkatesh"
for i in a:
    print(i)

# # Check if a string is a palindrome.
string="malayalam"
if string==string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# # Count how many times a character appears in a strin
x="puneeth"
print(x.count("e"))
print(x.index("e"))

# # Split a sentence into words
x="this is a city"
word=x.split()
print(word)

# # Join a list of words into a single string.
x=["this", "is", "a" ,"city"]
result=" ".join(x)
print(result)

# Remove all special characters from a string.
s = "Pu@ne#e!th123"

result = ""

for ch in s:
    if ch.isalnum():
        result += ch

print(result)


# Swap uppercase to lowercase and vice versa
s="Hello World"
print(s.swapcase())

p="puneeth"
result=""
for ch in p:
    if ch not in result:
        result+=ch
print(result)
