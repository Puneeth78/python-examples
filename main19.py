# square pattern
print("square pattern")
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()




# square parallel bar pattern
print("square parallel bar pattern")
n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# square + 
print("square + ")
n=5
for i in range(n):
    for j in range(n):
        if j==n//2 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# cross pattern
print("cross pattern")
n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# hallow square
print("hallow square")
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# increasing a triangle
print("increasing a triangle")
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

# decreasing a pattern
print("decreasing pattern")
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

# right sided triangle
print("right sided triangle")
def right_sided_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
print(right_sided_triangle(5))

# right sided triangle
print("right sided triangle")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

# hill pattern
print("hill pattern")
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

# hill pattern reverse
print("hill pattern reverse")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

# diamond pattern
print("dimond pattern")
n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

# hallow increasing triangle
print("hallow increasing triangle")
n=5
for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# hallow decreasing triangle
n=5
for i in range(n):
    for j in range(i,n):
        if i==0 or j==i or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# hallow hill pattern
print("allow hill pattern")
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if i==n-1 or j==0:
          print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i+1):
        if i==n-1 or j==i:
          print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# hallow diamond pattern
print("hollow diamond pattern")


# Upper Part
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")

    for j in range(i):
        if  j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for j in range(i+1):
        if  j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Lower Part
for i in range(n-2,-1, -1):
    for j in range(i,n):
        print(" ",end=" ")

    for j in range(i):
        if j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for j in range(i+1):
        if j==i:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()


n=4
m=5
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()

n=4
triangle=[]
for i in range(1,n+1):
    triangle.append("*"*n)
print(triangle)


print("hallow inverted triangle")
n=5
for i in range(n-2,-1, -1):
    for j in range(i,n):
        print(" ",end=" ")

    for j in range(i):
        if j==0 or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for j in range(i+1):
        if j==i:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()

# reverse pyramid
print("hill pattern reverse")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

print("Hollow Reverse Pyramid")
n = 5

for i in range(n):
    
    # left spaces
    for j in range(i):
        print(" ", end="")
    
    width = 2*(n-i) - 1   # total stars width
    
    for j in range(width):
        
        # first row full stars
        if i == 0:
            print("*", end="")
        
        # first and last star
        elif j == 0 or j == width - 1:
            print("*", end="")
        
        else:
            print(" ", end="")
    
    print()

