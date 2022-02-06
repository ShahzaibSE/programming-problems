#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here 
    a_max = max(a)
    b_min = min(b)
    count = 0
    for num in range(a_max, b_min+1):
        left = all([num % numA == 0 for numA in a])
        right = all([numB % num == 0 for numB in b])
        count += left * right
    return count

print(getTotalX([2,6], [24,36]))