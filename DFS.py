import sys

def iniciador ():
    lstF = []
    matrix = lector()
    
    #print(matrix)
    for i in range(0, len(matrix[0])):
        v = i
        lst = []
        lst.append(i)
        lst = adyacentes(matrix, lst, i)
        if lst == True:
            print(lst)
            return lst
        lstF.append(lst)
    print(lstF)

def lector()->list:
    matriz = []
    linea = list(map(str, sys.stdin.readline().split("	")))
    cont = len(linea)
    i = 0
    while(i < cont):
        j = 0
        lst = []
        while(j < cont):
            lst.append(int(linea[j]))
                #sys.stdout.writelines(linea[j]+" ")
            j+=1
        matriz.append(lst)
        #sys.stdout.writelines("\n")
        i += 1
        linea = list(map(str, sys.stdin.readline().split("	")))

    return matriz


def adyacentes(matrix, lst, i):
    for j in range(0, len(matrix[i])):
        if (matrix[i][j] != 0 and matrix[i][j] != -1):
            #print(lst)
            if lst == True:
                return True
            else:
                if j != lst[0] and j not in lst: 
                    lst.append(j)
                    lst = adyacentes(matrix, lst, j)
                else:
                    return True
        
    return lst



lst = [[0,90,80,-1,-1],
        [15,0,69,48,-1],
        [91,-1,0,12,39],
        [78,-1,-1,0,36],
        [-1,-1,-1,-1,0]]

lst1 = [[0,90,-1],
        [-1,0,69],
        [-1,-1,0]]

iniciador()
