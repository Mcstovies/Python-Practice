first_name = "adam"
last_name = "clarke"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# Whitespaces are commonly used to clean up user input before its stored in a program
favourite_language = 'python '
favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language = ' python'
favourite_language = favourite_language.strip()
print(favourite_language)