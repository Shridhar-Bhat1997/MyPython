# slicing --> create a substring by extracting elements from another string. (indexing or slicing) [:]
# starting index inclusive & stopping index exclusive


name="Rahul Dravid"
first_name=name[0:5]
print(first_name)

last_name=name[6:12]
print(last_name)

first_last=name[0:10:2] # [start:stop:step-size]
print(first_last)

reversed_name=name[::-1]
print(reversed_name)

website1="https://www.google.com"
website2="https://www.gmail.com"

slice1=slice(7,-4)
print(website1[slice1])

slice2=slice(3,-6)
print(website2[slice2])

 