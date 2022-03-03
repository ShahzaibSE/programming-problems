# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step 
# it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, 
# and each step up or down represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and 
# ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and 
# ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

from itertools import count


def countingValleys(steps, path):
    seaLevel = valleyCount = 0
    #
    for i in range(steps):
        if(path[i] == 'U'):
            seaLevel = seaLevel + 1
        else:
            seaLevel = seaLevel - 1
        if(path[i] == 'U' and seaLevel == 0):
            valleyCount = valleyCount + 1
    return valleyCount

print(countingValleys(8, "UDDDUDUU"))