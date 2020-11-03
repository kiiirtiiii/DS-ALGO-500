def median(matrix, r, c):
        sortedMatrix = []
        for i in range(r):
            for j in range(c):
                sortedMatrix.append(matrix[i][j])
                
        sortedMatrix.sort()
        
        return sortedMatrix[r*c//2]

r = 3
c = 3
matrix = [[1,3,5], [2, 6, 9], [3, 6, 9]]
print(median(matrix, r, c))


########### OUTPUT ###########
'''
5
'''