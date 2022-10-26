
from heapq import heapify, heappush
import sys

def iniciador(lst):
    matriz = lectorLst(lst)
    solu = dijkstra(matriz, 0)
    return solu



def lectorLst(lst):
    matriz = {}
    for i in range(0, len(lst)):
        dicc = {}
        for j in range(0, len(lst[i])):
            if lst[i][j] > 0:
                dicc[j] = lst[i][j]
        matriz[i] = dicc
    return matriz


def lector():
    matriz = {}
    linea = list(map(str, sys.stdin.readline().split("	")))
    cont = len(linea)
    i = 0
    while(cont != 0):
        cont-=1
        j = 0
        dicc = {}
        while(j < len(linea)):
            if linea[j] > 0:
                dicc[j] = linea[j]
            j+=1
        matriz[i] = dicc
        i += 1
        linea = list(map(str, sys.stdin.readline().split("	")))
    return matriz
    

def matrizPesos(matriz):
    inf = sys.maxsize
    dicc = {}
    for i in matriz:
        dicc[i] = {'costo':inf, 'anterior':""}
    return dicc

def dijkstra(matriz, ini):
    data = matrizPesos(matriz)
    data[ini]['costo'] = 0
    data[ini]['anterior'] = str(0)
    print(data)
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
                        print(costo)
                        data[j]['costo'] = costo
                        print(data[temp]['anterior'])
                        var = data[temp]['anterior']
                        data[j]['anterior'] = data[temp]['anterior']
                        data[j]['anterior'] += "-"+str(j)
                        print(data[j]['anterior'])
                    heappush(min_heap,(data[j]['costo'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    return data




lst = [[0,90,80,-1,-1],
        [15,0,69,48,-1],
        [91,-1,0,12,39],
        [78,-1,-1,0,36],
        [26,12,39,33,0]]

print(iniciador(lst))

