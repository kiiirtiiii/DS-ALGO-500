n = 3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("--- Original Matrix ---")

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print("")

print("--- Rotated Matrix ---")

# Transpose of a matrix
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Interchange columns from start and end
for i in range(n):
    for j in range(n//2):
        matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

# Printing a matrix
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print("")
    

####### OUTPUT #######
'''
--- Original Matrix ---
1 2 3
4 5 6
7 8 9
--- Rotated Matrix ---
7 4 1
8 5 2
9 6 3
'''