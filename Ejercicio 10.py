'''Escribir un programa que almacene la cadena de caracteres
 contraseña en una variable, pregunte al usuario por la 
 contraseña hasta que introduzca la contraseña correcta.'''

key = input("Crea tu contraseña: \n")
correcto = False
while correcto == False:
    contraseña = input("Introduce la contraseña \n")
    if contraseña == key:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")