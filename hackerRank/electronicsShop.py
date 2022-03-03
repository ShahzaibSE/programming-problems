# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. 
# Given price lists for keyboards and USB drives and a budget, find the cost to buy them. 
# If it is not possible to buy both items, return .

# Example

# The person can buy a , or a . Choose the latter as the more expensive option and return .

# Function Description

# Complete the getMoneySpent function in the editor below.

# getMoneySpent has the following parameter(s):

# int keyboards[n]: the keyboard prices
# int drives[m]: the drive prices
# int b: the budget
# Returns

# int: the maximum that can be spent, or  if it is not possible to buy both items

from curses import KEY_UNDO


# def getMoneySpent(keyboards, drives, b):
#     cost = 0
#     differences = {}
#     #
#     # if (len(keyboards) == len(drives)): 
#     for i in range(len(keyboards)): 
#             cost = keyboards[i] + drives[i]
#             differences[abs(b - cost)] = cost 
#     # return differences[min(differences.keys())]
#     return differences

def getMoneySpent(keyboards, drives, b):
    purchases = []
    #     
    for keyboard in keyboards:
        for drive in drives:
            cost = keyboard+ drive
            if (cost <= b):
                purchases.append(cost)
    if (not purchases):
        return -1
    else:
        return max(purchases)



print(getMoneySpent([40,50,60], [5,8,12], 60))
