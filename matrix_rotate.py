def rotateMat(mat):
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1
    
    while left < right and top < bottom:
        prev = mat[top+1][left]
        
        for i in range(left, right+1):
            current = mat[top][i]
            mat[top][i] = prev
            prev = current
            
        top += 1
        
        for i in range(top,bottom+1):
            current = mat[i][right]
            mat[i][right] = prev
            prev = current
        
        right -=1
        
        for i in range(right, left-1,-1):
            current = mat[bottom][i]
            mat[bottom][i] = prev
            prev = current
            
        bottom -=1
        
        for i in range(bottom, top-1, -1):
            current = mat[i][left]
            mat[i][left] = prev
            prev = current
        
        left +=1
    
    return mat


def printMatrix(mat):
    for row in mat:
        print (row)
        
        
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

mat = rotateMat(matrix)
printMatrix(mat)