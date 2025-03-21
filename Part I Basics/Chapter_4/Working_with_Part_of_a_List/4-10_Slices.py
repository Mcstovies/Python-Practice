# 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
#lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a 
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to 
# nprint the last three items in the list. 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a 
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to 
# print the last three items in the list.

pizzas = ['Black Pudding', 'Spicy Salami', 'Maggie', 'Vegan', 'Banana Curry']
print(f"The first three items in the list are: {pizzas}")
print(pizzas[0:3]) # Takes the first three items of the pizza list

print(f"Three items from the middle of the list are: {pizzas[1:3]}") # Prints the middle parts of the list

print(f"The last two items in the list are: {pizzas[3:5]}") # Prints the last items