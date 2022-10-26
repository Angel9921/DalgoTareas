import sys
import numpy as np

def lector()->dict:
    matriz = {}
    linea = list(map(str, sys.stdin.readline().split("	")))
    cont = len(linea)
    i = 0
    while(i < cont):
        j = 0
        dicc = {}
        while(j < cont):
            if int(linea[j]) > 0:
                dicc[int(j)] = int(linea[j])
                #sys.stdout.writelines(linea[j]+" ")
            j+=1
        matriz[int(i)] = dicc
        #sys.stdout.writelines("\n")
        i += 1
        linea = list(map(str, sys.stdin.readline().split("	")))

    return matriz

def floyd_warshall(grafo):
    
    lon = len(grafo)
    matriz = iniciar_matriz(lon)
    k = 0
    while(k < lon):
        i=0
        while(i < lon):
            j=0
            while(j < lon):
                if(k == 0):
                    if(i == j):
                        matriz[k][i][j] = 0
                    elif(grafo.get(i).get(j, "None") != "None"):
                        matriz[k][i][j] = int(grafo[i][j])
                else:
                    matriz[k][i][j] = min(matriz[k-1][i][j], matriz[k-1][i][k-1] + matriz[k-1][k-1][j])
                j+=1
            i+=1
        k+=1
    print(matriz)
    return matriz[lon-1]

def iniciar_matriz(longitud):
    matriz = np.empty((longitud, longitud, longitud), int)
    k = 0
    while(k < longitud):
        i = 0
        while(i < longitud):
            j = 0
            while(j < longitud):
                matriz[k][i][j] = int(32767*2)
                j += 1
            i += 1
        k += 1
    return matriz

grafo = lector()
floyd_warshall(grafo)