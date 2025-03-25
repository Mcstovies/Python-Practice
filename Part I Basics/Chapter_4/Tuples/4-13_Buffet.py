# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the 
# change.
# • The restaurant changes its menu, replacing two of the items with different 
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.

# Defining tuple
food = ("rice", "bread", "ham", "prawns", "noodles")
print("Original Menu:")
# Prints all items in the tuple
for foods in food:
    print(foods)

# Trying to modify one item but causes an error
# food[1] = "pasta"

# Assigning new values to the tuple 
food = ("pasta", "eggs", "ham", "prawns", "noodles")
print("\nModified Menu:")
for foods in food:
    print(foods)