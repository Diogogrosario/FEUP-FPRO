def zero_matrix(size):
    #Cria matriz com tudo a zeros
    result = []
    line = []
    for _ in range(0,size):
        line.append(0)
    for _ in range(0,size):
        result.append(line.copy())
    
    return result

def is_identity(mx):
    #Retorna True se uma matriz for a identidade
    result = True
    for i in range(0,len(mx)):
        if mx[i][i] != 1:
            result = False
            break
        elif mx[i].count(0) != len(mx)-1:
            result = False
            break
    return result
        
def transpose(mx):
    #Devolve a matriz transposta de uma matriz quadrada
    result = zero_matrix(len(mx))
    #Transpoe a matriz
    for i in range(0,len(mx)):
        for j in range(0,len(mx)):
            result[j][i] = mx[i][j]
        
    return result

def mult(mx1,mx2):
    #Multiplicação de duas matrizes quadradas da mesma dimensao(mx1*mx2)
    result = zero_matrix(len(mx1))

    for i in range(0,len(mx1)):
        for j in range(0,len(mx1)):
            for a in range(0,len(mx1)):
                    result[i][j] += mx1[i][a]*mx2[a][j]

    return result

def is_orthogonal(mx):
    #Verifica se uma matriz é ortogonal
    return is_identity(mult(mx,transpose(mx)))




print(is_orthogonal([[-2,3], [4,-1]]))
	