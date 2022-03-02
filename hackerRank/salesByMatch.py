# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example


# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs
from collections import Counter

def sockMerchant(n, ar):
    # pairs = [(a,b) for idx, a in enumerate(ar) for b in ar[idx + 1: ] if a == b]
    pair_count = 0
    sock_pairs = set()
    for i in range(len(ar)): 
        if(ar[i] not in sock_pairs):
           sock_pairs.add(ar[i])
        else:
            sock_pairs.remove(ar[i])
            pair_count = pair_count + 1
    return pair_count




print(sockMerchant(7, [1,2,1,2,1,3,2]))
