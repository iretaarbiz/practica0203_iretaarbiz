'''Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo
 al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre anterior a la M 
 y los hombres con un nombre posterior a la N y Slytheryn por el resto. 
 Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'''

nombre = input("Introduce tu nombre: \n")
sexo = input("Introduce tu sexo: \n")
if nombre[0] <= "M" and sexo.lower() == "mujer":
    print("Eres de Griffindor")
elif nombre[0] >= "N" and sexo.lower() == "hombre":
    print("Eres de Griffindor")
else:
    print("Eres de Slytherin")
