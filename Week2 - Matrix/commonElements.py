def commonElements(matrix, m, n):
    arr = dict()
    
    for j in range(n):
        arr[matrix[0][j]] = 1

    for i in range(1, m):
        for j in range(n):
            if (matrix[i][j] in arr.keys()) and (arr[matrix[i][j]]==i):
                arr[matrix[i][j]] = i+1
        
                if i==m-1:
                    print(matrix[i][j], end=" ")

    
m = 4
n = 5
matrix = [[1, 2, 1, 4, 8], [3, 7, 8, 5, 1], [8, 7, 7, 3, 1], [8, 1, 2, 7, 9]]
commonElements(matrix, m, n)


######## OUTPUT ########
'''
8 1
'''