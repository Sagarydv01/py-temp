""" # Grading System
marks = int(input("Enter marks: "))

if (marks >= 70) and (marks <= 100):
    if marks <= 90:
        print("B")
    else:
        print("A")
else:
    if marks < 70 and marks > 0:
        print("C")
    else:
        print("Invalid") """
    
""" # list
lst = [749, 48, "sagar", 'A', 43.3] # homogeneous 
marks = [36, 53, 32, 24, 55]
print(lst)
print(type(lst))

lst[1] = 948
print(lst)

lst.append(90) # insert element at last
print(lst)

print(lst[2:5]) # slicing

marks.reverse()
print("Reverse: ", marks)
marks.sort(reverse=True)
print("Sort list: ", marks)

print(lst.pop())
lst.remove('A') 
print(lst) """

""" # Tuple
tup = (34, '35', 36, 36, 63, 24)
tup2 = (56,)
tup3 = (1)
tup4 = ()

print(tup)
print(tup2)

print(type(tup))    # <class 'tuple'
print(type(tup2))   # <class 'tuple'>
print(type(tup3))   # <class 'int'>
print(type(tup4))   # <class 'tuple'>

print("Count of 36: ", tup.count(36))
print("Index of 36:", tup.index(36)) """


# List Palindrome
list = []

# list.append(input("Enter first element: "))
# list.append(input("Enter second element: "))
# list.append(input("Enter third element: "))
# list.append(input("Enter fourth element: "))
# list.append(input("Enter fifth element: "))

# for i in range(1, 6):
#     print("Enter element", i, ": ", end="")
#     list.append(input())

# cpList = list
# cpList.reverse()
# print(cpList)
# print(list)
# if list == cpList:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#
marks =[]
for i in range(1, 6):
    print("Enter marks of subject", i, ": ", end="")
    marks.append(int(input()))

marks.sort(reverse=True)
sum = 0

# for i in range(0,5):
#     sum += marks[i]

# avrg = sum/5
print("Highest marks:", marks[0])
# print("Average marks:", avrg)
print("Average marks:", marks[2])
print("Lowest marks:", marks[4])

