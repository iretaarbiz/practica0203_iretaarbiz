'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo que tenga tantas líneas como el número introducido, como el triángulo de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

num = int(input("Introduce un número entero: \n"))
for i in range(num):
    for j in range(1, 2 * (i + 1)):
        if j % 2 == 1: 
            print(2 * (i + 1) - j, end="")
    print(end="\n")