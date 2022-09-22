# dictionary --> a collection which is changeable,unordered,unique key:value pairs.

capitals={"USA":"Washington",
          "India":"Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}

print(capitals["India"]) # to access the value
print(capitals.get("Germany")) # used to check key is present in dictionary or not.
print(capitals.keys()) # print all the keys
print(capitals.values())# print all the values
print(capitals.items()) # print both key & value.

for key,value in capitals.items():
    print(key,value)
    
capitals.update({"Germany":"Berlin"}) # to add item
print(capitals)

capitals.update({"USA":"Las Vegas"}) # to update new value
print(capitals)

capitals.pop("China")
print(capitals)

