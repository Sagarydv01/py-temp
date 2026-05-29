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
    
# list
lst = [749, 48, "sagar", 'A', 43.3] # homogeneous 
print(lst)
print(type(lst))

lst[1] = 948
print(lst)

lst.append(90) # insert element at last
print(lst)

print(lst[2:5]) # slicing