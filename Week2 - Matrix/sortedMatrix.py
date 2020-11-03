T = int(input())
for _ in range(T):
    n = int(input())
    matrix = list(map(int, input().split()))
    matrix.sort()
    for i in matrix:
        print(i, end=" ")
    print("")


########## OUTPUT ##########
'''
2
4
10 20 30 40 15 25 35 45 27 29 37 48 32 33 39 50
10 15 20 25 27 29 30 32 33 35 37 39 40 45 48 50       # Output

3
1 3 4 2 6 7 5 8 9
1 2 3 4 5 6 7 8 9       # Output
'''