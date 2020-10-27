T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    rotatedArr = ['*' for i in range(n)]

    i = -1
    m = -n-1
    
    while i!=m:
        rotatedArr[i+1] = arr[i]
        i -= 1
        
    for j in rotatedArr:
        print(j, end=" ")
    print("")


########## OUTPUT ##########
'''
2                   # Number of test cases
5                   # Length of an array
1 2 3 4 5           # Given array
5 1 2 3 4           # Rotated array
8                   # Length of an array
9 8 7 6 4 2 1 3     # Given array
3 9 8 7 6 4 2 1     # Rotated array
'''