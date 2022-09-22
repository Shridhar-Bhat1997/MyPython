# list --> used to store multiple items in a single variable & it is mutable.

food=["mango","apple",22,"grapes"]
print(food)
print(food[2])

food[0]="banana"
print(food)

food.append("ice") # add items at the end
print(food)

food.remove(22) # to remove item
print(food)

food.insert(2,"papaya") # insert an item at specified index
print(food)

food.sort() # sort the items alphabetically
print(food)

food.pop(1) #  removes the element at the specified position
print(food)

items=["hello","bye"]
items.clear() # removes all the elements from the list.
print(items)