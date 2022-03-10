# A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, and 
# the characters have a maximum height they can jump. 
# There is a magic potion they can take that will increase their maximum jump height by  unit for each dose. 
# How many doses of the potion must the character take to be able to jump all of the hurdles. 
# If the character can already clear all of the hurdles, return .

# Example


# The character can jump  unit high initially and must take  doses of potion to be able to jump all of the hurdles.

# Function Description

# Complete the hurdleRace function in the editor below.

# hurdleRace has the following parameter(s):

# int k: the height the character can jump naturally
# int height[n]: the heights of each hurdle
# Returns

# int: the minimum number of doses required, always  or more

def unique_arr(arr): 
    unique_arr = []
    for ele in arr:
        if ele not in unique_arr:
            unique_arr.append(ele)
    return sorted(unique_arr)

def hurdleRace(k, hurdles):
    # Write your code here
    # hurdle_heights = sorted(list(set(hurdles)))
    # print(hurdle_heights)
    if(k > max(hurdles)): return 0
    else: 
        return max(hurdles) - k
    #
    
  

print(hurdleRace(1,[1,2,3,3,2]))
print(hurdleRace(4,[1,6,3,5,2]))
print(hurdleRace(7,[2,5,4,5,2]))
