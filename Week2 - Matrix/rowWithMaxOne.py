def rowWithMax1s(arr, n, m):
    maximum = 0
    maximumIndex = -1
    for i in range(n):
        if arr[i].count(1)>maximum:
            maximumIndex = i
            maximum = arr[i].count(1)

    return maximumIndex

n = 4
m = 4
arr = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
print(rowWithMax1s(arr, n, m))


######### OUTPUT #########
'''
2
'''