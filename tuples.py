#tuple = collection which is ordered and unchangealbe used to group together related data.

student = ("Herman",25,"male")

print(student.count("Herman"))
print(student.index("male"))

for x in student:
    print(x)

if "Herman" in student:
    print("Herman is here.")
else:
    print("Herman is not here")