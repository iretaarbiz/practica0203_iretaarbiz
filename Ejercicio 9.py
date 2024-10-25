'''Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo que tenga tantas líneas como el 
número introducido, como el triángulo de más abajo.'''
num = int(input("Introduce un número entero: \n"))
for i in range(num):
    for j in range(2 * (i + 1), 1, -2):
            print(j-1, end=" ")
    print(end="\n")