Student = {
    "rno" : 1,
    "name" : ["Sagar", "Aman"],
    "age" : [21, 19],
    "course" : ["MCA", "BSc"]
}

print(Student["name"][0])
print(Student.get("name"))

print("Keys:", Student.keys())
print("Values:", Student.values())

Student.update()
print(Student)










