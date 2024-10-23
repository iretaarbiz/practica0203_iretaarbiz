'''Escribir un programa en el que se pregunte al usuario por una frase y 
una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.'''

frase = input("Dame una frase: \n")
letra = input("Dame una letra: \n")
vecesletra = 0
for i in range(len(frase)):
    if letra == frase[i]:
        vecesletra += 1
print("La letra", letra, "aparece", vecesletra, "veces en la frase introducida")
