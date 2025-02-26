# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program


# Beginning of list and the first people to be invited

people = ['Lauren', 'Charlie', 'Lewis']
message = f'Hey {people[0]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[1]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[2]}, I would like to invite you to din dins.'
print(message)

# Message to know I have found a bigger table and can invite more

table = 'Hey everyone! I have found a bigger table so we can invite more people.'
print(table)

# Inserting three people into the list

people.insert(0, 'Helen')
print(people)

people.insert(2 , 'Alfie')
print(people)

people.append('Three Wee Guys')
print(people)

# Messages to everyone invited
print(f'Hey {people[0]}, I would like to invite you to din dins.')
print(f'Hey {people[1]}, I would like to invite you to din dins.')
print(f'Hey {people[2]}, I would like to invite you to din dins.')
print(f'Hey {people[3]}, I would like to invite you to din dins.')
print(f'Hey {people[4]}, I would like to invite you to din dins.')
print(f'Hey {people[5]}, I would like to invite you to din dins.')

# Message to say I can only invite a few

print("Sorry to all but the table wont arrive in time so I can only invite two of you")

# no_invite variable to pop people out of the list and a message to let them know

no_invite = people.pop(0)
print(f'Sorry {no_invite} but I cannot invite you this time.')
no_invite = people.pop(1)
print(f'Sorry {no_invite} but I cannot invite you this time.')
no_invite = people.pop(2)
print(f'Sorry {no_invite} but I cannot invite you this time.')
no_invite = people.pop(2)
print(f'Sorry {no_invite} but I cannot invite you this time.')

# Letting the two people know they are still invited

print(f'Hey {people[0]}, I can still invite you to dinner.')
print(f'Hey {people[1]}, I can still invite you to dinner.')

# Deleting the final two people to leave list empty

del people[0]
print(people)
del people[0]
print(people)

