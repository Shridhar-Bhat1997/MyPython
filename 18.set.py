# set --> collection which is unordered,unindexed and no duplicate values.

utensils={"spoon","fork","knife"}
dishes={"bowl","plate","cup","spoon"}

for x in utensils:
    print(x)
    
utensils.add("napkin") 
print(utensils)

utensils.update(dishes)
print(utensils)

dinner_table=utensils.union(dishes)
print(dinner_table)

print(utensils.difference(dishes))

print(utensils.intersection(dishes))
print(utensils)
print(dishes)
