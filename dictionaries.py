#Dictionaries = a changeable, unordered collection of unique key: value pairs
#               Fast because they use hashing, allow us to access a value quickly.
capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}
#print(capitals["Germany"]) #stops the program
#print(capitals.get("Germany")) #Gives value "None"
#print(capitals.keys()) Prints the first information key.
#print(capitals.values()) Prints the value stored inside the key.
#print(capitals.items()) Prints everything.

#for key,value in capitals.items():
#    print(key,value) Prints entire dictionary
capitals.update({"Germany":"Berlin"}) #adds new information
capitals.update({"USA":"Las Vegas"}) #change current information
capitals.pop("China") #Removes the "Key", China.
#capitals.clear()  Clears the dictionary.

for key,value in capitals.items():
    print(key,value)
