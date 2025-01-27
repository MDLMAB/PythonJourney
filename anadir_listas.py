"""  
Formar una lista x con elementos de la lista a múltiplos de 3

"""

# Método 1: 

a = ['a', "a0", "a1" , 'b' , "b2", "b3" , 'c', "c4", "c5", 'd', "d6","d7"]
x = []
for w in range(len(a)):
    if w % 3 == 0:
        x.append(a[w])

print(f" La lista resultante: {x} ")

# Método 2:
# Utilizando list comprehension
x2 = [a[w2] for w2 in range(len(a)) if w2 % 3 == 0] 