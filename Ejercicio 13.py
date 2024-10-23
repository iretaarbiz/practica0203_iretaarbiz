'''Escribir un programa que muestre el eco de todo lo que el usuario
 introduzca hasta que el usuario escriba “salir” que terminará.'''

salir = False
while salir == False:
    entrada = input("Introduce el texto que desees mostrar: ")
    if entrada != "salir":
        print(entrada)
    else:
        salir = True