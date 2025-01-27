# Elaborar una lista y eliminar un elemento de la misma
import random
import pdb as debug   # Librería para debug
import time 
time_init = time.time()
# Crear la variable lista con 0 elementos
lista = []

# Unir a la lista valores aleatorios
for i in range(0,9):
    lista.append(round(random.random(),2))
print(f" La lista original es: {lista}")
dimension_inicial = len(lista)
# Eliminar el último elemento de la lista 
# El método pop() te devuelve por consola el elemento eliminado
lista.pop() 
# print(lista)

print(f" Visualización: {lista} " )
valor_aleatorio = round(random.random(), 2)

# Eliminar un elemento de la lista coincidente con el valor indicado
# debug.set_trace()
try:
    encontrado = False
    for j in range(len(lista)):
        if encontrado == True:
            j -=1
            encontrado = False
        else:
            j = j
        
        if lista[j] == valor_aleatorio:
            # print(f" Hay una coincidencia en la lista ")
            lista.remove(valor_aleatorio)
            # print(lista)
            encontrado = True
        else:
            None
            # print(f" ¡¡Mala suerte!! Prueba suerte a la proxima ")
            # print(lista)
except IndexError:
    print(f"Las dimensiones de la lista han cambiado")
    print(f"Inicialmente tuvo {dimension_inicial} elementos, ahora tiene {len(lista)}")

print(f" Lista final: {lista}")
# time.time() devuelve el tiempo en segundos desde el epoch 1 enero 1970
# Para calcular el tiempo de ejecución basta con restar los segundos actuales - segundos al iniciar el script
print(f" El tiempo de ejecución del programa es {round((time.time() - time_init),5)} s")