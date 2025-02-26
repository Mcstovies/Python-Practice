# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

people = ['Lauren', 'Charlie', 'Lewis']
message = f'Hey {people[0]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[1]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[2]}, I would like to invite you to din dins.'
print(message)
table = 'Hey everyone! I have found a bigger table so we can invite more people.'
print(table)
people.insert(0, 'Helen')
print(people)
people.insert(2 , 'Alfie')
print(people)
people.append('Three Wee Guys')
print(people)
message = f'Hey {people[0]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[1]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[2]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[3]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[4]}, I would like to invite you to din dins.'
print(message)
message = f'Hey {people[5]}, I would like to invite you to din dins.'
print(message)
