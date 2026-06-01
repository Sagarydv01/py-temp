
# program to find a number in a tuple
num = ()
lst = []

for i in range(0, 5):
    print("Enter", i+1, "number: ", end="")
    lst.append(int(input()))

num = tuple(lst)
print(num)

print("Enter number to find in tuple:")
val = int(input("Enter value to find: "))

if val in num:
    print("Found at index", num.index(val))
else:
    print("Not found!")

# -------------------------------------------------
