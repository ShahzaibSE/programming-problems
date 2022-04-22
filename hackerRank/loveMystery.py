# James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

# To do this, he follows two rules:

# He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
# The letter  may not be reduced any further.
# Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

# Example

# The following two operations are performed: cde → cdd → cdc. Return .

# Function Description

# Complete the theLoveLetterMystery function in the editor below.

# theLoveLetterMystery has the following parameter(s):

# string s: the text of the letter
# Returns

# int: the minimum number of operations

def theLoveLetterMystery(s):
    for index in range(len(s)):
        if(s[index] == 'a'):
            continue
        if(index == 0):
            continue


print(theLoveLetterMystery('cde'))