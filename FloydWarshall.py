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
    for i in grafo:
        print(i)
        for j in grafo[i]:
            print(str(j)+ ":" + str(grafo[i][j]))

    matriz = iniciar_matriz(lon)
    #print(grafo)
    #print(grafo[0][1])
    k = 0
    while(k < lon):
        i=0
        while(i < lon):
            j=0
            while(j < lon):
                if(k == 0):
                    #print("k igual a 0")
                    #print(grafo[i])
                    #print("i es igual a " +str(i))
                    #print("j es igual a "+str(j))
                    if(i == j):
                        matriz[k][i][j] = 0
                    elif(grafo.get(i).get(j, "None") != "None"):
                        matriz[k][i][j] = int(grafo[i][j])
                else:
                    #print("k diferente de 0")
                    matriz[k][i][j] = min(matriz[k-1][i][j], matriz[k-1][i][k-1] + matriz[k-1][k-1][j])
                j+=1
            i+=1
        k+=1
    
    # i = 0
    # while(i < lon):
    #     j = 0
    #     while(j < lon):
    #         k = 0
    #         while(k < lon):
    #             sys.stdout.write(str(matriz[i][j][k])+" ")
    #             k+=1
    #         print("\n")
    #         j+=1
    #     print("\n")
    #     print("==========")
    #     i+= 1

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