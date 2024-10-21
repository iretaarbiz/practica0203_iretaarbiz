'''Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad 
y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.'''

edad = int(input("Introduce tu edad: \n"))
ingresos = int(input("Introduce tus ingresos mensuales: \n"))
if edad >= 16:
    if ingresos >= 1000:
        print("Debes tributar")
    else:
        print("No debes tributar")
else:
        print("No debes tributar")