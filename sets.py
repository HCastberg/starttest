#set = collection which is unoordered, unindexed. No duplicate values.

from lib2to3.pgen2.tokenize import untokenize


untensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#untensils.add("napkin")
#untensils.remove("fork")
#untensils.clear()
#untensils.update(dishes)
#dinner_table = untensils.union(dishes)
print(untensils.difference(dishes))
print(dishes.difference(untensils))

print(untensils.intersection(dishes)) #in common

#for x in dinner_table:
#    print(x)