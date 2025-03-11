locations = ['Tokyo', 'Rome', 'Falklands', 'Hong Kong', 'Seoul']
print(locations)
print(sorted(locations)) # Sorts list temporarily with sorted()
print(locations) # Showing that its still in its original form
print(sorted(locations,reverse=True)) # Reverses list temporarily
print(locations) # Shows list in its original form




# Printing list in its original form
locations = ['Tokyo', 'Rome', 'Falklands', 'Hong Kong', 'Seoul']
print(locations) 
locations.reverse() #Reverses original list
print(locations)
locations.reverse() # Puts list back to its original form
print(locations)
locations.sort() # Stores in alphabetical order
print(locations)
locations.sort(reverse=True)# Reverse-alphabetical order
print(locations)