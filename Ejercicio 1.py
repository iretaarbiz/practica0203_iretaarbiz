'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. '''

clave = input("Crea la contraseña: \n")
contra = input("Introduce la contraseña: \n")
if contra.lower() == clave.lower():
    print("La contraseña introducida coincide")
else: 
    print("La contraseña introducida no coincide")