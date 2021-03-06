def transpose(matrix):
    r=len(matrix)
    c=len(matrix[0])
    transpose=[]
    for i in range(c):
        mat=[]
        for j in range(r):
            mat.append(matrix[j][i])
        transpose.append(mat)
    return transpose
                
        