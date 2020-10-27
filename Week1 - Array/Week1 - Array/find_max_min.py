# Maximum and minimum of an array using minimum number of comparisons:

def maxMin(arr):                        # In this algo we are comparing pair of two elements with another pair of two element
    if len(arr)%2==0:
        maximum = max(arr[0], arr[1])
        minimum = min(arr[0], arr[1])

        i = 2

    else:
        maximum = minimum = arr[0]

        i = 1

    while i<len(arr)-1:
        maximum = max(maximum, max(arr[i], arr[i+1]))
        minimum = min(minimum, min(arr[i], arr[i+1]))

        i += 2

    return [maximum, minimum]
        
arr = list(map(int, input().split()))
maxAndMin = maxMin(arr)
print("Maximum: "+str(maxAndMin[0]))
print("Minimum: "+str(maxAndMin[1]))


##################### OUTPUT #####################
'''
1000 11 445 1 330 3000
Maximum: 3000
Minimum: 1
'''