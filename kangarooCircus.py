#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if (x1 > x2 and v1 > v2):
        return "NO"
    elif (x1 < x2 and v1 < v2):
        return "NO"
    if (v2 < v1 and (x2 - x1) % (v2 - v1) == 0 ) == 0:
        return "NO"
    else:
        return "YES"

print(kangaroo(0,3,4,2))