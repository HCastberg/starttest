#logical operators (and,or,not) = used to check if two or more conditional statements are true.

temp = int(input("What is the temperature outside?: "))

if temp>=0 and temp <=30:
    print("The temperature is good today!")
    print("Go outside!")

elif not(temp < 0 or temp >30):
    print("The temperature is bad today!")
    print("Stay inside!")

#not - reverses the inside
#if not(temp>=0 and temp <=30):
#    print("The temperature is good today!")
#    print("Go outside!")