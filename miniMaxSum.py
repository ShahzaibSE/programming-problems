def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    # 
    print()
    print("Min sum")
    for num in range(len(arr)-1):
        print(arr[num])
        min_sum += arr[num]
    #
    print()
    print("Max sum")
    for num in range(1, len(arr)):
        print(arr[num])
        max_sum += arr[num]
    #
    print()
    print("{} {}".format(min_sum, max_sum))    

miniMaxSum([1,3,5,7,9])
miniMaxSum([7, 69, 2, 221, 8974])

def miniMaxSumV2(arr):
    arr.sort()
    s = sum(arr)
    maxResult = s - arr[0]
    minResult = s - arr[len(arr) - 1]
    print("{} {}".format(minResult, maxResult))   

miniMaxSumV2([1,3,5,7,9])
miniMaxSumV2([7, 69, 2, 221, 8974])

