import time
time_init = time.time()
tabla_del = int(input(" ¿Qué tabla de multiplicar practicamos hoy? "))
# Variable contenedor para almacenar los resultado, variable lista vacía
tabla = []
# Bucle que se repite 10 veces
for i in range(0, 11):
    print(f" {tabla_del} x {i} = {tabla_del * i}")
    tabla.append(tabla_del * i)
print(f" Aqui tenemos los resultados de la tabla de multiplicar: {tabla} ")
print(f" El tiempo de ejecución del programa es {round((time.time() - time_init),13)} s")