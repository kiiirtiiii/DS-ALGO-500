# Given an array and there is only one duplicate number in nums, return this duplicate number.

#### Follow-ups: ####

# How can we prove that at least one duplicate number must exist in nums? 
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n2)?

def duplicacy(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])]>=0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            return abs(arr[i])

arr = list(map(int, input().split()))
print(duplicacy(arr))


########### OUTPUT ###########
'''
3 1 3 4 2
3
'''