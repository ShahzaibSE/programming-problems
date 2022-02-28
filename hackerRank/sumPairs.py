# Given an array of integers and a positive integer , determine the number of  pairs where  and  +  is divisible by .

# Example



# Three pairs meet the criteria:  and .

# Function Description

# Complete the divisibleSumPairs function in the editor below.

# divisibleSumPairs has the following parameter(s):

# int n: the length of array 
# int ar[n]: an array of integers
# int k: the integer divisor
# Returns
# - int: the number of pairs

def divisibleSumPairs(n,k,ar): 
    pair_count = 0
    pairs = []
    if(len(ar)<=n):
        # print("The original list : " + str(ar))
        pairs = [(a,b) for idx, a in enumerate(ar) for b in ar[idx + 1: ]]
        # print('Pairs: '+str(pairs))
        #    
        for i in range(len(pairs)):
            sumPair = pairs[i][0] + pairs[i][1]
            if(sumPair % k == 0):
                pair_count = pair_count + 1
                # print(pair_count)
    return pair_count

result = divisibleSumPairs(6,5,[1,2,3,4,5,6])
print("Number of divisible pairs: {}".format(result))
    