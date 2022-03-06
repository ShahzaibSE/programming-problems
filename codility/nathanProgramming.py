import math

def solution(T, R):
    # write your code in Python 3.6
    try:
        if(len(T) == len(R)):
            test_cases = []
            print(T)
            # txt = "h3110 23 cat 444.4 rabbit 11 2 dog"
            # nums = [int(s) for s in T.split() if s.isdigit()]
            for ele in T:
                print(ele.split(''))
                # test.clear()

            print(test_cases)
            print(nums)
            return  2 * 100 // 3
        else:
            return 0
    except:
        print('Unknown Error')

print(solution(['test1a', 'test2', 'test1b', 'test1c', 'test3'], ['Wrong Answer', 'OK', 'Runtime error', 'OK', 'time limit exceeded']))