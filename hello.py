""" # print("Sagar Yadav"); print("Sagar") # SyntaxError
print("Sagar Yadav"); print("Sagar") # use semicolon to separate instruction/expression in a line

# dynamically typed language
greet = "hello"

num1 = input("Enter a number: ")        #32
num2 = input("Enter another number: ")  #43
print(num1 + num2)  #3243
# input() method treat values "String" by default

# we need to typecast for others
num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))
print(num3 + num4)

num3 = float(input("Enter a number: "))
num4 = float(input("Enter another number: "))
print(num3 + num4)

print("num1 = ", num1) """

""" 
sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))

print("Average marks: ", ((sub1+sub2+sub3)/3))

# conditional statements
if sub1<sub2:
    print("sub1 ",sub1)
    #   print("Sagar!") # IndentationError: unexpected indent
    print("IF")
elif sub1>sub2:
    print("Elif")
else:
    print("ELSE")
 """

# Q. Find number is negative, positive or zero
num = int(input("Enter a num: "))

print("Num is ", end= "")
if num < 0:
    print("Negative")
elif num > 0:
    print("Positive")
else:
    print("Zero")