# Using variables in strings

first_name = "adam"
last_name = "clarke"
full_name = f"{first_name} {last_name}" # f-strings(format) 
message = f"Hello, {full_name.title()}!" # Title changes case in a string
print(message)

# Whitespaces are commonly used to clean up user input before its stored in a program

favourite_language = 'python '
favourite_language = favourite_language.rstrip() # Removes extra space from the right side
print(favourite_language)

favourite_language = ' python'
favourite_language = favourite_language.lstrip() # Removes extra space from the left side
print(favourite_language)

favourite_language = ' python'
favourite_language = favourite_language.strip() # Removes extra space from both sides
print(favourite_language)

# Removing Prefixes

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

