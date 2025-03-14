# 4-6. Odd Numbers: Use the third argument of the range() function to make a list 
# of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = range(1, 21, 2) # Skips every even number and only includes odd ones

for odd_number in odd_numbers:
    print(odd_number)