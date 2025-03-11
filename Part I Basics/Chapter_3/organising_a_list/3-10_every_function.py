# 3-10. Every Function: Think of things you could store in a list. For example, you 
# could make a list of mountains, rivers, countries, cities, languages, or anything 
# else you’d like. Write a program that creates a list containing these items and 
# then uses each function introduced in this chapter at least once.

# Changes the order of the list permanently into alphabetical order
uk = ['Scotland', 'England', 'Wales', 'Northern Ireland']
uk.sort()
print(uk)

# Reverses list permanently
uk.sort(reverse=True)
print(uk)

# Sorting list temporarily
uk = ['Scotland', 'England', 'Wales', 'Northern Ireland']
print(sorted(uk))
print(uk)

# Reverses temporarily
uk = ['Scotland', 'England', 'Wales', 'Northern Ireland']
print(sorted(uk,reverse=True))
print(uk)

print(len(uk))



