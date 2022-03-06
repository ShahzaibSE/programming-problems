
import statistics

def solution(A, S):
    # write your code in Python 3.6
    fragment = 0
    if((min(A)>=-1000000000 and max(A)<=1000000000) and (S>=-1000000000 and S<=1000000000)):
        fragment = sum(A) / len(A)
        if(fragment > 1000000000):
            return 1000000000
        else:
            rounded_fragment = round(fragment)
            if(rounded_fragment == S):
                return rounded_fragment
            else:
                return 0


print(solution([2,1,3], 2))
print(solution([0,4,3,-1], 2))
print(solution([2,1,4], 3))
#
print(solution([1,4,4,5], 3))
