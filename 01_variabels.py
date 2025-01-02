# There are plenty of variables in Python.
# In this course, we will learn the most common ones.

firstname = 'Any Name';
lastname = 'Any Last Name';
print(firstname, lastname)

# Python does not support the cammel case for variables.
''' Python does support the snake case for variables. 
    For example, firstname is okey but first_name is better.'''

city = 'Any Place';
age = 25;

print(city, age)

my_int_variable = 10;
print(my_int_variable) 
print(type(my_int_variable)) # DATA TYPE <class 'int'>

my_bool_variable = True;
print(my_bool_variable)

if my_bool_variable:
    print('This is a True value')
else:
    print('This is a False value')


print("My name is ", firstname, lastname, "I'm from ", city, "and I'm ", age, "years old.")

# What we can do is to use functions to print the message.
# We can use the format() function to replace the variables in the string.
my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))
# System fuctions
    # How does len() work?
print(len(firstname)) 
''' The len() function returns the number of characters in a string.'''
name, username = 'Mercedes', 'MDLMAV'

print('My name is {} and my username is {}'.format(name, username))
print('I live in {}'.format(city))
print('I enjoy learning Python and I am {} years old'.format(age))
firstname = input('Whats your name?') # This is a string displayed by console
print('I enjoy learning Python and I am {} years old'.format(firstname))

firstname = 123
print('I enjoy learning Python and I am {} years old'.format(firstname))