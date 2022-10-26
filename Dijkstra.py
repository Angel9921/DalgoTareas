
from heapq import heapify, heappush
import sys

def iniciador():
    matriz = lector()
    for i in matriz:
        solu = dijkstra(matriz, i)
        print("Para vertice iniciando en " + str(i) + " los costos caminos minimos son: " + str(solu)+ "\n")
    



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

def matriz_pesos(matriz):
    inf = sys.maxsize
    dicc = {}
    for i in matriz:
        dicc[i] = {'costo':inf, 'anterior':""}
    return dicc

def dijkstra(matriz, ini):
    data = matriz_pesos(matriz)
    data[ini]['costo'] = 0
    data[ini]['anterior'] = str(ini)
    visitados = []
    temp = ini
    for i in range(0,len(data)-1):
        if temp not in visitados:
            visitados.append(temp)
            min_heap = []
            for j in matriz[temp]:
                if j not in visitados:
                    costo = data[temp]['costo'] + matriz[temp][j]
                    if costo < data[j]['costo']:
                        data[j]['costo'] = costo
                        var = data[temp]['anterior']
                        data[j]['anterior'] = data[temp]['anterior']
                        data[j]['anterior'] += "-"+str(j)
                    heappush(min_heap,(data[j]['costo'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    return data


iniciador()

