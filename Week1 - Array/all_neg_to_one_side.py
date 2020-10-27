# Move all negative numbers to beginning and positive to end with constant extra space

arr = list(map(int, input().split()))
negative = []
positive = []

for i in arr:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)

finalArr = negative + positive

for j in finalArr:
    print(j, end=" ")


########### OUTPUT ###########
'''
-12 11 -13 -5 6 -7 5 -3 -6
-12 -13 -5 -7 -3 -6 11 6 5
'''