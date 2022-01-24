#function = a block of code which is executed only when it is called.

from os import name


def hello(first_name,last_name,age):
    print("Hello " + first_name + last_name)
    print("You are "+ str(age) + " years old")
    print("Have a nice day")

#hello("Herman")
#hello("Dude")
#my_name = "Herman"


hello("Herman ","Castberg",25)