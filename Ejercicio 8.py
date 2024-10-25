''' Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.'''

for i in range(1, 11):
    print("-----------") #Para separar de la tabla de un número a la tabla de otro
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)