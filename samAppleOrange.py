#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # print('Apple distances')
    apple_counter = 0
    orange_counter = 0
    for d in apples:
        if(a+d >= s and a+d <= t):
            apple_counter += 1
    # print('Orange distances')
    for d in oranges:
        if(b+d >= s and b+d <= t):
            orange_counter += 1
    print(apple_counter)
    print(orange_counter)