""" 
Definir una clase Calculo_Numerico que nos permita llevar a cabo varias operaciones numéricas. Esta clase tiene un solo atributo: un número entero.
La clase atributo debe contener un constructor y varios métodos de operaciones matemáticas. 

"""

class Calculo_Numerico:
    def __init__(self, numero):                         # Definición del constructor   
        self.numero = numero                            # Atributo de la clase: número entero

    def calculo_factorial(self):                        # Método para calcular el factorial de un número: el numero factorial de un número entero n 
        if self.numero < 0:                             # es el producto de todos los números enteros positivos menores o iguales a n.  
            print("No se puede calcular el factorial de un número negativo")
        else:
            factorial = 1
            for i in range(1, self.numero + 1):
                factorial = factorial * i
            return factorial
        
    def lista_divisores(self):                          # Método para calcular los divisores de un número entero
            divisores = []                              # Almacenar los divisores en una lista
            for i in range(1, self.numero + 1):
                if self.numero % i == 0:                # Si el número es divisible por i, entonces i es un divisor de self.numero
                    divisores.append(i)                 # Añadir i a la lista de divisores
            return divisores
        
    def esPrimo(self):                                  # Método para determinar si un número entero es primo                 
            if self.numero < 2:                         # Un número primo es un número entero mayor que 1 que no tiene divisores positivos distintos de 1 y de sí mismo.
                return False
            for i in range(2, self.numero):
                if self.numero % i == 0:
                    return False
            return True
        
    def esPar(self):                                    # Método para determinar si un número entero es par
            if self.numero % 2 == 0:                    # Un número entero es par si es divisible por 2
                return True
            else:
                return False
                                                        # Casos de uso: instanciar la clase y llamar a los métodos
x = int(input("Introduce un número entero: "))
primer_calculo = Calculo_Numerico(x)
factorial = primer_calculo.calculo_factorial()
print(f"El factorial de {x} es: {factorial}")
divisor = primer_calculo.lista_divisores()
print(f"Los divisores de {x} son: {divisor}")
esprimo = primer_calculo.esPrimo()        
print(f"¿El número {x} es primo?: {esprimo} ")
espar = primer_calculo.esPar()
print(f"¿El número {x} es par?: {espar}")
