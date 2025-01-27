# Learning strings in Python
# Strings are a sequence of characters.
# Strings are immutable.
# Strings can be sliced.
# Strings can be concatenated.
# Strings can be formatted.
# Strings can be compared.
# Strings can be converted.
# Strings can be transformed.
# Strings can be checked.
# Strings can be searched.
# Strings can be replaced.
# Strings can be splitted.
# Strings can be joined.

my_string = '\tHello, World!' # \t is a tab
my_other_string = "Hello, World! \nThis is a new line."  # \n is a new line
my_name = 'Mercedes'
my_username = 'MDLMAV'
my_age = 28
print(my_string)
print(my_other_string)
# Strings can be formatted.
print('My name is {} and my username is {}'.format(my_name, my_username))
print('I am {} years old'.format(my_age))
print(f'I am {my_age} years old')
print('***********************')

lenguage = 'mercedes'
for letter in lenguage:
    print(letter)
for letter in lenguage[:-3]:
    print(letter)

print(lenguage.capitalize())
print(lenguage.upper().replace('s', 'x'))
print(lenguage.lower().replace('e', 'a'))
print(lenguage.count('e'))
print(lenguage.replace('e', 'a'))
print(lenguage.startswith('mi'))
print(lenguage.endswith('es'))