import numpy as np

def spiralMatrix(arr, m, n):
    begRow = 0
    endRow = m-1
    begCol = 0
    endCol = n-1
    
    while begRow<=endRow and begCol<=endCol:
        
        for j in range(begCol, endCol+1):
            print(arr[begRow][j], end=" ")
        
        begRow += 1
                
        for i in range(begRow, endRow+1):
            print(arr[i][endCol], end=" ")
            
        endCol -= 1
        
        if begRow<=endRow:
            for j in range(endCol, begCol-1, -1):
                print(arr[endRow][j], end=" ")
                
        endRow -= 1
        
        if begCol<=endCol:
            for i in range(endRow, begRow-1, -1):
                print(arr[i][begCol], end=" ")
                
        begCol += 1
    print("")
    
T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    
    entries = list(map(int, input().split()))
    arr = np.array(entries).reshape(m, n)
    
    spiralMatrix(arr, m, n)
    

########### OUTPUT ###########
'''
2       

4 4    
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10  # Spiral Matrix

3 4
1 2 3 4 5 6 7 8 9 10 11 12

1 2 3 4 8 12 11 10 9 5 6 7  # Spiral Matrix
'''