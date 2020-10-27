# Write a program to reverse an array:

arr = list(map(int, input().split()))

reversedArr = [0 for i in range(len(arr))]

j = len(reversedArr)-1

for i in arr:
	reversedArr[j] = i
	j -= 1

print("Given Array: ", end="")
print(arr)
print("Reversed Array: ", end="")
print(reversedArr)


##################### OUTPUT #####################
'''
1 2 3
Given Array: [1, 2, 3]
Reversed Array: [3, 2, 1]
'''