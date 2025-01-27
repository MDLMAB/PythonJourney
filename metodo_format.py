# Ejercicios con método format()
import random

lista = []
for i in range(10):
    num_random = random.random()
    if i < 5:
        lista.append(round(num_random,3))
    else:
        abcd = "abcd"
        cambiar_letra = random.randrange(0,3,1)
        lista.append(abcd[cambiar_letra])

print(f" Elaboramos una Lista con datos numéricos y letras: {lista}")

txt5 = "{0:.2f}, {6!r}, {9!r}".format(*lista)
print(f" Tras formatear la lista, queda: {txt5} ")
