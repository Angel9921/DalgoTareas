
import sys

def iniciador(lst):
    grafo = lector2(lst)
    lista = []
    validados = ""
    for i in grafo:
        if str(i) not in validados:
            salida = bfs(grafo, i)
            lista.append(salida[0])
            validados += salida[1]
    print(lista)


def bfs(grafo, v):
    visitados = []
    cola = []
    visitados.append(v)
    cola.append(v)
    validados = ""
    while cola:
        a = cola.pop(0)
        for vertice in grafo[a]:
            if vertice not in visitados:
                visitados.append(vertice)
                validados += str(vertice)
                cola.append(vertice)
    return (visitados, validados)


def lector2(lstM):
    dicc = {}
    for i in range(0,len(lstM)):
        lst = []
        for j in range(0,len(lstM[i])):
            if lstM[i][j] > 0:
                lst.append(j)
        dicc[i] = lst
    return dicc



def lector()->dict:
    matriz = {}
    linea = list(map(str, sys.stdin.readline().split("	")))
    cont = len(linea)
    i = 0
    while(i < cont):
        j = 0
        lst = []
        while(j < cont):
            if linea[j] > 0:
                lst.append(j)
                #sys.stdout.writelines(linea[j]+" ")
            j+=1
        matriz.append(lst)
        #sys.stdout.writelines("\n")
        i += 1
        linea = list(map(str, sys.stdin.readline().split("	")))

    return matriz


lst = [[-1,-1,-1,1,-1,-1,-1],
        [-1,-1,-1,-1,-1,1,-1],
        [-1,-1,-1,1,-1,-1,-1],
        [1,-1,1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,1],
        [-1,1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,1,-1,-1]]


iniciador(lst)

