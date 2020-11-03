def searchMatrix(matrix, target):
    i = 0
    j = -1
    
    if len(matrix)>0:
        if len(matrix[0])>0:
            while i<len(matrix):
                if target < matrix[i][-1]:
                    j = i
                    break
                elif target == matrix[i][-1]:
                    return 1
                i += 1

            if j!=-1:
                for k in matrix[j]:
                    if k==target:
                        return 1

                return 0

            else:
                return 0
    else:
        return 0


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(bool(searchMatrix(matrix, target)))

######### OUTPUT #########
'''
True
'''