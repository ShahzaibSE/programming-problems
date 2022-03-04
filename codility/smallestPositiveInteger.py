# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def unique_list(arr):
    unique_arr = []
    #   
    for i in range(len(arr)):
        if (arr[i] not in unique_arr):
            unique_arr.append(arr[i]) 
    #
    return unique_arr


def solution(A):
   a=frozenset(sorted(A))
   m=max(a)
   if m>0:
       for i in range(1,m):
           if i not in a:
              return i
       else:
          return m+1
   else:
       return 1

print(solution([1, 3, 6, 4, 1, 2]))