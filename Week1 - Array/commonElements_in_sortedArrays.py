class Solution:
    def commonElements (self, A, B, C, n1, n2, n3):
        i, j, k = 0, 0, 0
        arr = []
        
        while i<n1 and j<n2 and k<n3:
            if A[i]==B[j] and B[j]==C[k]:
                if A[i] not in arr:
                    arr.append(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i]<B[j]:
                i += 1
            elif B[j]<C[k]:
                j += 1
            else:
                k += 1
                
        return arr

# Driver code Starts {

t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends


######### OUTPUT #########
'''
1
6 5 8
1 5 10 20 40 80
6 7 20 80 100
3 4 15 20 30 70 80 120

20 80   # Output
'''