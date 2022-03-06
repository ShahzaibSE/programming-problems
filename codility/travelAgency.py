# Time Complexity: O(2*N)
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    if(n >= 1 and n<=100000):
        hash_set = dict()
        max_count = len(set(A))
        i = 0
        j = 0
        result = float("inf")

        while i < n:

            if A[i] in hash_set:
                hash_set[A[i]] += 1
            else:
                hash_set[A[i]] = 1
            if len(hash_set) == max_count:
                result = min(result, i-j)
            
            while len(hash_set) == max_count and j<=i:
                hash_set[A[j]] -= 1
                if hash_set[A[j]] == 0:
                    del hash_set[A[j]]
                    j+=1
                if len(hash_set) < max_count:
                    break
                result = min(result, i-j)

                if result == max_count:
                    return result
                j+=1
            i+=1
        return result
    else:
        return 0


print(solution([2,1,1,3,2,1,1,3]))