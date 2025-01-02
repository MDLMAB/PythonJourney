# Here we will learn about lists in python
# Lists are ordered collection of items
# Lists are mutable
# Lists are dynamic
# Lists are defined by square brackets []

my_list = list([1,2,3,4] ) # A list is a structure that can store multiple items
print(my_list)
my_other_list = [12, 16, 87.5, 55,67, 55, 0.70] # An empty list
print(my_other_list)
print(len(my_list))
print(len(my_other_list))
print(max(my_other_list))
print(type(my_other_list))
print(my_other_list.count(16))
print(my_other_list.index(55))
a, b, c, d, e, f, g = my_other_list
print(a, b, c, d, e, f, g)

print(my_list + my_other_list)
my_list.append(5)
my_list.insert(2,10)
print(my_list)
my_pop_element = my_list.pop()
print(my_pop_element)

lista_de_compra = list(['leche', 'pan', 'huevos', 'jamon', 'queso'])
lista_de_compra.append('papel higienico')
print(lista_de_compra)
for item in lista_de_compra:
    print(item)

my_new_list = lista_de_compra.copy()
lista_de_compra.clear()
my_new_list.reverse()
my_new_list.sort()
print(lista_de_compra)
print(my_new_list)