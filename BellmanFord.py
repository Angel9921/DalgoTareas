import sys

def iniciador():
    matriz = lector()
    for i in matriz:
        solu = bellman(matriz, i)
        print("vertice "+ str(i) + " = " + str(solu))
    

def bellman(matriz, ini):
    infi = sys.maxsize    
    data = matriz_pesos(matriz)
    data[ini]['costo'] = 0
    data[ini]['anterior'] = str(ini)
    for key in matriz:
        for adya in matriz[key]:
            costo = data[key]['costo'] + matriz[key][adya]
            if(costo < data[adya]['costo']):
                data[adya]['costo'] = costo
                data[adya]['anterior'] = data[key]['anterior']
                data[adya]['anterior'] += "-"+str(adya)
    return data

        



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


iniciador()