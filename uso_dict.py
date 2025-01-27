# Uso de diccionarios. Aplicación de métodos de la clase diccionario
# Prueba debug

# Crear un diccionario con frutas y sus precios
frutas = {"Manzana": 0.5, "Pera": 2.0, "Naranja": 1.0}
print(frutas)                                           # Imprimir el diccionario
print(type(frutas))                                     # Tipo de dato del diccionario   
print(frutas["Pera"])                                   # Obtener el valor de la key "Pera"

# Permitir sumar los valores del diccionario

colores = dict(rojo = 5.8, azul = 2, verde = 3.5)       # Crear un diccionario con colores y sus precios
print(colores)                                          # Imprimir el diccionario
print(type(colores))                                    # Tipo de dato del diccionario

# Sumar los valores del diccionario

sum = (frutas["Manzana"] * colores["rojo"] + frutas["Pera"] * colores["verde"])
print(f" La suma de los valores de los diccionarios es: {sum} ")

# Utilización del método format()

precio_real = 5.5 * 1.1055999
print(f" El precio real es: {precio_real} ")
print(f" El precio real es: {precio_real:.2f} ")
print(f" El precio real es: {precio_real.format()} ") 