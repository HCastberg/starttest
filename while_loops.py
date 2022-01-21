#while loops = a statement that will execute it's block of code as long as it's code is true.

#Two different types

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello "+ name)


name2 = None
while not name2:
    name2 = input("Enter your name: ")
print("Hello "+ name2)