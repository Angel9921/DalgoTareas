
def iniciador (matrix):
    lstF = []
    for i in range(0, len(matrix[0])):
        v = i
        lst = []
        lst.append(i)
        lst = adyacentes(matrix, lst, i)
        print(lst)
        lstF.append(lst)
    return lstF


# def booleanLst(lstF, v):
#     b = False
#     for i in range(0, len(lstF)):
#         if v in lstF[i]:
#             b = True
#     return b


def adyacentes(matrix, lst, i):
    for j in range(0, len(matrix[i])):
        if (matrix[i][j] != 0 and matrix[i][j] != -1):
            if j not in lst:
                lst.append(j)
                lst = adyacentes(matrix, lst, j)
            else:
                lst.append(j)
        
    return lst



lst = [[0,90,-1,-1,-1],
        [15,0,-1,48,-1],
        [-1,-1,0,-1,39],
        [78,-1,-1,0,-1],
        [-1,-1,-1,-1,0]]

lst1 = [[0,90,80],
        [-1,0,69],
        [-1,-1,0]]

print(iniciador(lst))
