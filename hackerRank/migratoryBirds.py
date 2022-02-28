# Given an array of bird sightings where every element represents a bird type id, 
# determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, 
# return the smallest of their ids.

# Example

# There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .

# Function Description

# Complete the migratoryBirds function in the editor below.

# migratoryBirds has the following parameter(s):

# int arr[n]: the types of birds sighted
# Returns

# int: the lowest type id of the most frequently sighted birds

from collections import Counter
import operator
import sys

def migratoryBirds(arr): 
    # Write your code here
    count = [0] * 6
    for i in arr:
        count[i] += 1
    return count.index(max(count))


def unique_list(arr):
    unique_arr = []
    #   
    for i in range(len(arr)):
        if (arr[i] not in unique_arr):
            unique_arr.append(arr[i]) 
    #
    return unique_arr

def migratoryBirds(arr): 
    unique_birds = []
    bird_freq = 0
    bird_frequencies = []
    #   
    unique_birds = unique_list(arr)
    #    
    for i in range(len(unique_birds)):
        for j in range(len(arr)):
            if(unique_birds[i] == arr[j]):
                bird_freq = bird_freq + 1
        bird_frequencies.append(bird_freq)
        bird_freq = 0
    print(bird_frequencies)
    bird_id = unique_birds[bird_frequencies.index(max(bird_frequencies))]
    return bird_id


# print(migratoryBirds([1,1,2,2,3]))
print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))


