import random
import sys


jugadas = 0
matrix = []
    

f = input('hola! te voy a pedir que ingreses la cantidad de filas que quieres que tenga tu programa: ')
c = input('Ahora te pedire que ingreses la cantidad de columnas, debe ser la misma cantidad de filas: ')

for i in range(int(f)):
    fila = []  
    for e in range(int(c)):
        coordenadas = (i, e)
        fila.append(coordenadas)
    matrix.append(fila)

for i in range(len(matrix)):
    for e in range(len(matrix)):
        print(f'Ingrese un numero a la matriz en la posicion {i,e}')
        matrix[i][e] = int(input())
        

numeroaleatorio1 = random.randint(0, int(f)-1)
numeroaleatorio2 = random.randint(0, int(c)-1)
matrix[numeroaleatorio1][numeroaleatorio2] = '*'



while True:
    x = int(input('Tu objetivo es intentar adivinar donde se encuentra el caracter "*" , intenta poniendo 2 numeros el primero en coordenada x => '))
    y = int(input('ahora pon la segunda coordenada en eje y => '))
    if ((x < 0) or (x > len(matrix))) or ((y < 0) or y > len(matrix)):
        print(f'te fuiste del tablero debes poner un numero entre {0} en rango x y {len(matrix)-1} en rango y')
    elif matrix[x][y] == '*':
        sys.exit(print(f'Felicitaciones has ganado'))
    else:
        jugadas +=1
        print(f'Erraste ya realizaste {jugadas} jugadas')
    
    





