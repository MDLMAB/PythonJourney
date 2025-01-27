my_sets = set() # Create an empty set structure
print(type(my_sets)) # <class 'set'> defined
my_other_sets = {} # Create an empty dictionary structure
# Dictionary items can be defined as key:value pairs.
print(type(my_other_sets)) # <class 'dict'> defined
# Sets are unordered, so you cannot be sure in which order the items will appear.
my_other_sets = {'Mercedes', 1.73, 9.8, 2, 1.73 }
print(type(my_other_sets)) # <class 'set'> defined
print(len(my_other_sets)) # 4
print(my_other_sets) #  Unordered, changeable and indexed. No duplicate members.
my_other_sets.add('MDLMAV') # Add an item to the set
print(my_other_sets) # {1.73, 2, 9.8, 'Mercedes', 'MDLMAV'}
my_other_sets.add('MDLMAV') # Add an item that already exists in the set
print(my_other_sets) # {1.73, 2, 9.8, 'Mercedes', 'MDLMAV'}

my_other_sets.add('mdlmav') # Add an item that already exists in the set
print(my_other_sets) 
# Adding multiple items to a set is not possible. But you can add items from another set, list, tuple or dictionary.
# my_other_sets.remove('MDLMAV') # Remove an item from the set
# print(my_other_sets) # {1.73, 2, 9.8, 'Mercedes'}
print("Carretero" in my_other_sets) # False
print("Carretero" not in my_other_sets) # True
my_other_sets.update(['Carretero', 'muchacha', 'muchacho']) # Add multiple items to the set
print(my_other_sets) 
my_list_of_sets = list(my_other_sets) # Convert the set into a list
print(my_list_of_sets)
print(my_list_of_sets[2])
my_other_sets.discard('Carretero') # Remove an item from the set
print(my_other_sets) 
my_other_sets.clear() # Remove all items from the set
print(my_other_sets) # set()
del my_other_sets # Delete the set completely
print(my_other_sets) # This will raise an error because the set no longer exists
