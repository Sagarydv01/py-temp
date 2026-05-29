# print("hello")
# print(23+3)
# name = "Sagar"
# age = 21
# print(name, age)
# print(type(name))

# age = int(input("Enter age: "))

# print("Your age is greater than 18:", age > 18)

""" 
num1 = 332
num2 = 32

# arithmetic operator
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 // num2)
print(num1 * num2)
print(num1 % num2)
print(2 ** 5) 
"""
#-----------------------------
# assignment operator
# ----------------------------
# a = 5
# a = a + 5 # a += 5
# print(a)

# b = 5
# b %= 3
# print(b)

""" a = 10
b = 20
c = 4

#------------------------------
# logical operator
#------------------------------
print(not (a > b))
print((a < b) and (b < c))
print((a < b) or (a < c)) """

""" 
if not (a > b):
    print("not")
elif (a < b) and (b < c):
    print("and")
elif (a < b) or (a < c):
    print("or") """

""" #---------------------------------
# implicit conversion
d = a/2
print(d)

# explicit/type casting
d = int(d)
print(d)
#--------------------------------- """

name = "Sagar Yadav"
# print(len(name))

# print(name[0:6])
# print(name[:6])
# print(name[3:])
# print(name[-3:-5])
# print(name[2::2])

# print(name.endswith("v"))
# print(name.endswith("d"))

# print(name.replace('a', 'f'))
# print("Hello".replace("l", 'e'))

# print(name.find("a"))

# b = "This is India"
# c = name + " " +  b
# print(c.count("is"))

""" 
# 1. area of square
side = float(input("Enter side of square:"))
print("Area of square:", side * side)

# 2. Average of 3 nums
num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))
num3 = int(input("Enter 3rd num: "))

print("Average of 3 nums:", (num1 + num2 + num3)/3)

# 3. Traffic Light System
signal = input("Enter light color: ")

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
elif signal == "green":
    print("GO")
else :
    print("INVALID COLOR") """

# May 29, 2026
# Grading System
marks = int(input("Enter marks: "))

if (marks >= 70) and (marks <= 100):
    if marks <= 90:
        print("B")
    else:
        print("A")
else:
    if marks < 70:
        print("C")
    else:
        print("Invalid")
    
    