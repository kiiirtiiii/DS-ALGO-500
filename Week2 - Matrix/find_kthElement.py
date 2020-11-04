def kthSmallest(mat, n, k):
    sortedMatrix = []
    
    for i in range(n):
        for j in range(n):
            sortedMatrix.append(mat[i][j])
            
    sortedMatrix.sort()
    
    return sortedMatrix[k-1]

n = 4   
mat = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
k = 3
print(kthSmallest(mat, n, k))


########### OUTPUT ###########
'''
27
'''