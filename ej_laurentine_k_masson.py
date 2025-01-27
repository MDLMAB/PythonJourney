# Ejercicio 39 - Laurentine K. Masson -
""" 
Escribir una función llamada anadirElementoDicc(Clave, valor, d) que tome tres parámetros de entrada:
un diccionario d, una clave y su valor asociado. 
La función debe permitir agregar esta clave y su valor al diccionario d. Por último, la función debe devolver el diccionario d 
que contiene la nueva clave.

""" 

def anadirElementoDicc(clave, valor, d = {}):
    d[clave] = valor
    return d

# Test 
any_dic = {"any_girl_name": 19, "any_boy_name": 32, "any_girl_name": 27}
ej_39 = anadirElementoDicc("any_boy_name", 89, any_dic)
print(type(ej_39))
print(ej_39)

# Ejercicio 40  - Laurentine K. Masson -
""" 
Escribir una función máximo(L) que tome una lista de enteros como parámetro y devuelva el mayor valor.
Nota: La idea es no usar la función max()
""" 

def maximo(L=[]):
    num = []
    for i in range(len(L)):
        if i == 0:
            num.append(L[0])
        else:
            if L[i] > num[0]:
                num.pop()
                num.append(L[i])
            else:
                num = num
    return num[0] 

# Test
ej_40 = [12, -2, 4, 5] # El valor máximo en esta lista es 12

test_40 = maximo(ej_40)
print(test_40)

# Ejercicio 42  - Laurentine K. Masson -
""" 
Escribir un programa que muestre una pirámide de estrellas

""" 
def imprimeEstrellas(num_filas):
    for j in range(num_filas):
        estrellas = print((j + 1) * '*')
    return estrellas

filas = int(input(" Inserta fila de estrellas: "))
imprimeEstrellas(filas)




