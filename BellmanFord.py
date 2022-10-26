import sys

def iniciador(lst):
    matriz = lectorLst(lst)
    for i in matriz:
        solu = bellman(matriz, i)
        print("vertice "+ str(i) + " = " + str(solu))
    

def bellman(matriz, ini):
    infi = sys.maxsize    
    data = matrizPesos(matriz)
    data[ini]['costo'] = 0
    data[ini]['anterior'] = str(ini)
    for key in matriz:
        for adya in matriz[key]:
            costo = data[key]['costo'] + matriz[key][adya]
            if costo < data[adya]['costo']:
                data[adya]['costo'] = costo
                if data[adya]['costo'] == infi:
                    data[adya]['anterior'] = data[key]['anterior']
                    data[adya]['anterior'] += "-"+str(adya)
                else:
                    data[adya]['anterior'] = ""
                    data[adya]['anterior'] = data[key]['anterior']
                    data[adya]['anterior'] += "-"+str(adya)
    return data

        



def lectorLst(lst):
    matriz = {}
    for i in range(0, len(lst)):
        dicc = {}
        for j in range(0, len(lst[i])):
            if lst[i][j] != 0 and lst[i][j] != -1:
                dicc[j] = lst[i][j]
        matriz[i] = dicc
    return matriz


def matrizPesos(matriz):
    inf = sys.maxsize
    dicc = {}
    for i in matriz:
        dicc[i] = {'costo':inf, 'anterior':""}
    return dicc


lst = [[0,6,4,5,0,0],
        [-1,0,-1,-1,-2,-1],
        [91,-1,0,12,39,],
        [78,-1,-1,0,36,],
        [26,12,39,33,0,],
        [-1,-1,-1,-1,-1,0]]

lst2 = [[0,90,80,-1,-1],
        [15,0,69,48,-1],
        [91,-1,0,12,39],
        [78,-1,-1,0,36],
        [26,12,39,33,0]]

print(iniciador(lst2))