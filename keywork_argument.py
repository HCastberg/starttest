#keyword arguments = Arguments preceded by an identifier when we pass them to a function
#                      The order of the arguments doesn't matter, unlike positional arguments
#                       Python know the names of the arguments that our function recievs.


def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Castberg",first="Herman",middle="Oslo")