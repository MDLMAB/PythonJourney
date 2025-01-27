""" 

Prueba debugging. La libreria pdb permite hacer debugging en Python.
El inteprete se detendrá en la línea pdb.set_trace() y se podrán inspeccionar las variables
También se podrán ejecutar comandos e ir debuggeando el código línea por línea

"""
import pdb 
val_lst = [6,8,33,4,1,12,2,9.2]  

# Método 1: 
L = []                                              # Inicializar lista vacía
memory_val_lst = val_lst.copy()                     # Copiar la lista original

for i in range(len(val_lst)):
    eval_min = min(memory_val_lst)                  # Encontrar el valor mínimo de la lista
    L.append(eval_min)                              # Agregar el valor mínimo a la lista L
    memory_val_lst.remove(eval_min)                 # Remover el valor mínimo de la lista original

print(f" Lista original: {val_lst} ")
print(f" Lista ordenada en orden creciente: {L} ")

# Método 2: 
# Utilizando la función sort()
val_lst_2 = [6,8,33,4,1,12,2,9.2] 


print(f" Ahora se va a producir un break")
pdb.set_trace()   


print(f" Lista original: {val_lst_2} ")               
val_lst_2.sort()                                    # val_lst_2.sort() Modifica la lista original
print(f" Lista ordenada con implementacion sort(): {val_lst_2} ")



""" 

Ordenar una lista en orden descendiente

"""
# Método 3:     
M = []                                              # Inicializar lista vacía
memory_val_lst2 = val_lst.copy()                     # Copiar la lista original

for i in range(len(val_lst)):
    eval_max = max(memory_val_lst2)                  # Encontrar el valor mínimo de la lista
    M.append(eval_max)                              # Agregar el valor mínimo a la lista L
    memory_val_lst2.remove(eval_max)                 # Remover el valor mínimo de la lista original

print(f" Lista ordenada en orden decreciente: {M} ")

# Método 4: 
# Utilizando la función sort(reverse=False) por defecto el parámetro reverse es False
val_lst_3 = [6,8,33,4,1,12,2,9.2]                   
val_lst_3.sort(reverse=True)                                    # val_lst_3.sort(reverse=True) modifica la lista original en orden descendiente
print(f" Lista ordenada con implementacion sort(): {val_lst_3} ")