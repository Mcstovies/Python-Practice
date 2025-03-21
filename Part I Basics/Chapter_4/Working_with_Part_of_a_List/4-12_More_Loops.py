# 4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing, to save space. Choose a version of foods.py, and 
# write two for loops to print each list of foods.

# Original list of foods
my_foods = ['pizza', 'falafel', 'carrot cake']

# Copies original list for friends_foods list
friend_foods = my_foods[:]

# Prints the OG list 
print("My favourite foods are:")
for food in my_foods:
    print(food)

# Prints friends favourite food as well
print("\nMy friend's favourite food is:")
for food in friend_foods:
    print(food)