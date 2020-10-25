# Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order:

def sortedArray(A, N):
    B = ["*" for x in range(N)]
    
    zeros = A.count(0)
    ones = A.count(1)
    
    for i in range(zeros):
        B[i] = 0
    for j in range(zeros, ones+zeros):
        B[j] = 1
    for k in range(ones+zeros, N):
        B[k] = 2
        
    return B
        
T = int(input("Number of TestCases: "))
for _ in range(T):
    N = int(input("Number of elements in an Array: "))
    print("Elements of an Array:")
    A = list(map(int, input().split()))
    
    finalArray = sortedArray(A, N)
    print("Sorted Array: ", end="")
    for i in finalArray:
        print(i, end=" ")
    print("")


##################### OUTPUT #####################
'''
Number of TestCases: 2
Number of elements in an Array: 5
Elements of an Array:
0 2 1 2 0
Sorted Array: 0 0 1 2 2
Number of elements in an Array: 3
Elements of an Array:
0 1 0
Sorted Array: 0 0 1
'''