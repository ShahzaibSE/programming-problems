# Function Description

# Complete the birthday function in the editor below.

# birthday has the following parameter(s):

# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month
# Returns

# int: the number of ways the bar can be divided


def birthday(s,d,m):
    cnt = 0
    q = s[:m-1]
    for ele in s[m-1:]:
        q.append(ele)
        if (sum(q) == d):
            cnt += 1
        q.pop(0)
    return cnt

print(birthday([2,2,1,3,2], 4, 2))