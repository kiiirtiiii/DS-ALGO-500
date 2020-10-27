T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    setA = set(A)
    setB = set(B)
    
    unionSet = setA.union(setB)
    print(len(unionSet))


############## OUTPUT ##############
'''
2               # Number of test cases
5 3             # Length of array "A" and "B"
1 2 3 4 5       # Array "A"
1 2 3           # Array "B"
5               # Output
6 2             # Length of array "A" and "B"
85 25 1 32 54 6 # Array "A"
85 2            # Array "B"
7               # Output
'''