# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal 
# to.

# Example


# There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

# Function Description

# Complete the pickingNumbers function in the editor below.

# pickingNumbers has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the length of the longest subarray that meets the criterion

def pickingNumbers(arr):
    result = 0
    checked = set()
    for i in range(len(arr)):
        if i not in checked:
            maxCount = max(arr.count(arr[i]) + arr.count(arr[i] + 1), arr.count(arr[i]) + arr.count(arr[i] - 1))
            if maxCount > result:
                result = maxCount
            checked.add(i)
    return result


print(pickingNumbers([1,1,2,2,4,4,5,5,5]))