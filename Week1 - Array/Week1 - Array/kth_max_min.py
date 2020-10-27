# Given an array and a number K where K is smaller than size of array.
# The task is to find the Kth smallest element in the given array. 
# It is given that all array elements are distinct.

def kthSmallest(arr, K):
    arr.sort()
    return arr[K-1]

T = int(input("Number of Test Cases: "))
for _ in range(T):
    N = int(input("Number of elements in an Array: "))
    print("Enter elemenyts of Array: ")
    arr = list(map(int, input().split()))
    K = int(input("Kth number: "))
    
    print(str(K)+' smallest element is: ', end="")
    print(kthSmallest(arr, K))


##################### OUTPUT #####################
'''
Number of Test Cases: 2
Number of elements in an Array: 6
Enter elemenyts of Array:
7 10 4 20 15
Kth number: 3
3 smallest element is: 10
Number of elements in an Array: 5
Enter elemenyts of Array:
7 4 20 3 15
Kth number: 4
4 smallest element is: 15
'''