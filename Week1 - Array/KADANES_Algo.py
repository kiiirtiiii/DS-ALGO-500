# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

def maxSubArraySum(A, N):
    arr = [0 for i in range(N)]
    
    i = 0
    s = 0
    
    while i<N:
        arr[i] = max(A[i], A[i]+s)
        s = arr[i]
        i += 1
        
    return max(arr)

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(maxSubArraySum(A, N))


############# OUTPUT #############
'''
2               # Test cases
5               # Size of an array
1 2 3 -2 5      # Array
9               # Maximum contiguous subarray sum
4               # Size of an array
-1 -2 -3 -4     # Array
-1              # Maximum contiguous subarray sum
'''