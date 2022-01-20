#slicing = create a substring by extractiong elements from another string
#       indexing[] or slice()
#       [start:stop:step]


print("indexing") #indexing[]

name = "Herman Castberg"
first_name = name[:6] # 0 to 6
last_name = name[7:]  #7 to end
fynky_name = name[::2] #start to end with steps
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(fynky_name)
print(reversed_name)
print( )


print("slicing") #slicing()
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4,)

print(website1[slice])
print(website2[slice])