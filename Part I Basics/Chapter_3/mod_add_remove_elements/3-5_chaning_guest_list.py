# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list

people = ['Lauren', 'Charlie', 'Lewis']
message = f'Hey {people[0]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[1]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[2]}, I would like to invite you to din dins.'
print(message)
print(people[1]) # prints Charlie onto console
del people[1] # removes Charlie from the list
people.insert(1, 'Helen') # inserts new name into between Lauren and Lewis in the list
print(people) # prints out the new list
message = f'Hey {people[0]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[1]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[2]}, I would like to invite you to din dins.'
print(message)
