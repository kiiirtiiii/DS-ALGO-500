def merge(intervals):
    intervals.sort()
    N = len(intervals)
    x = 0
    while x<N-1:
        if intervals[x][-1]>=intervals[x+1][0] and intervals[x][-1]<=intervals[x+1][-1]:
            intervals[x] = [intervals[x][0], intervals[x+1][-1]]
            intervals.remove(intervals[x+1])
            
            N -= 1
            
        elif intervals[x][-1]>=intervals[x+1][0] and intervals[x][-1]>=intervals[x+1][-1]:
            intervals.remove(intervals[x+1])
            
            N -= 1
            
        else:
            x += 1
        
    return intervals

n = int(input("Number of set of intervals: "))
intervals = []
print("Enter sets")
for _ in range(n):
    a = list(map(int, input().split()))
    intervals.append(a)

print(merge(intervals))

########### OUTPUT ###########
'''
Number of set of intervals: 4
Enter sets
1 3
2 6
8 10
15 18
[[1, 6], [8, 10], [15, 18]]
'''