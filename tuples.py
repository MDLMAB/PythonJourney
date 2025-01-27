# What is a Tuple?
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

my_tuple = tuple()
print(my_tuple)
my_other_tuple = ('Mercedes', 1.73, 9.8, 2, 1.73 )
print(my_other_tuple)
# Access Tuple Items
print(my_other_tuple[0])
print(type(my_other_tuple))
print(my_other_tuple.count(1.73))
print(my_other_tuple.index(1.73))
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Change Tuple Values
# Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# Loop Through a Tuple
for z in my_other_tuple:
    print(z)
# Check if Item Exists
if 1.73 in my_other_tuple:
    print('Yes, 1.73 is in the tuple')
# Tuple Length
print(len(my_other_tuple))
# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
del my_other_tuple # Delete the tuple completely
print(my_other_tuple) # This will raise an error because the tuple no longer exists
