# In this problem we consider unsigned 30-bit integers, i.e. all integers B such that 0 ≤ B < 230.

# We say that integer A conforms to integer B if, in all positions where B has bits set to 1, A has corresponding bits set to 1.

# For example:

# 00 0000 1111 0111 1101 1110 0000 1111(BIN) = 16,244,239 conforms to
# 00 0000 1100 0110 1101 1110 0000 0001(BIN) = 13,032,961, but
# 11 0000 1101 0111 0000 1010 0000 0101(BIN) = 819,399,173 does not conform to
# 00 0000 1001 0110 0011 0011 0000 1111(BIN) = 9,843,471.
# Write a function:

# def solution(A, B, C)

# that, given three unsigned 30-bit integers A, B and C, returns the number of unsigned 30-bit integers conforming to at least one of the given integers.

# For example, for integers:

# A = 11 1111 1111 1111 1111 1111 1001 1111(BIN) = 1,073,741,727,
# B = 11 1111 1111 1111 1111 1111 0011 1111(BIN) = 1,073,741,631, and
# C = 11 1111 1111 1111 1111 1111 0110 1111(BIN) = 1,073,741,679,
# the function should return 8, since there are 8 unsigned 30-bit integers conforming to A, B or C, namely:

# 11 1111 1111 1111 1111 1111 0011 1111(BIN) = 1,073,741,631,
# 11 1111 1111 1111 1111 1111 0110 1111(BIN) = 1,073,741,679,
# 11 1111 1111 1111 1111 1111 0111 1111(BIN) = 1,073,741,695,
# 11 1111 1111 1111 1111 1111 1001 1111(BIN) = 1,073,741,727,
# 11 1111 1111 1111 1111 1111 1011 1111(BIN) = 1,073,741,759,
# 11 1111 1111 1111 1111 1111 1101 1111(BIN) = 1,073,741,791,
# 11 1111 1111 1111 1111 1111 1110 1111(BIN) = 1,073,741,807,
# 11 1111 1111 1111 1111 1111 1111 1111(BIN) = 1,073,741,823.
# Write an efficient algorithm for the following assumptions:

# A, B and C are integers within the range [0..1,073,741,823].
N = 30
def size(num):
    zeroes = sum(1 for bit in range(N) if (num >> bit) & 1 == 0)
    return 2**zeroes

def solution(a,b,c):  
    A = size(a)
    B = size(b)
    C = size(c)
    #    print((A >> 2) & 1)
    #    print(B >> 2)
    #    print(C >> 2)
    #    print(a)
    #    print(b)
    #    print(c)
    total = A + B + C
    total -= size(a | b) # counted twice, remove one
    print("A | B: {}".format(total))
    total -= size(b | c) # counted twice, remove one
    print("B | C: {}".format(total))
    total -= size(a | c) # counted twice, remove one
    print("A | C: {}".format(total))
    total += size(a | b | c) # counted three times, removed three times, add one
    print("A | B | C: {}".format(total))
    return total


print("Conforming Bit Masks")
print(solution(0b1001,0b0111,0b0110))
# print("Number of unsigned 30-bit integers conforming to at least one: ".format(solution(9,3,4)))

# print((2 >> 2) + (4 >> 2))