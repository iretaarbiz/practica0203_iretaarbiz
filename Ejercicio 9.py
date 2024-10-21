num = int(input("Introduce un número entero: \n"))
for i in range(1, num+1):
    for j in range(1, i, 2):
        print(j, end="")