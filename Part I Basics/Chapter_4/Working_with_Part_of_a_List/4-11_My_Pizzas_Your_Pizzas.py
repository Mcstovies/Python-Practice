# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).  
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the 
# following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite piz
# zas are:, and then use a for loop to print the first list. Print the message My 
# friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.


pizzas = ['Black Pudding', 'Spicy Salami', 'Maggie', 'Banana Curry']

friend_pizzas = ['Black Pudding', 'Spicy Salami', 'Maggie', 'Vegan']

# Print message
print("My favourite pizzas are: ")

# Loop through and print every pizza
for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizzas are: ")

for pizzas in friend_pizzas:
    print(pizzas)
