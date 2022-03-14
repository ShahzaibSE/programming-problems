# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

# There is a list of  character heights aligned by index to their letters. 
# For example, 'a' is at index  and 'z' is at index . There will also be a string. 
# Using the letter heights given, determine the area of the rectangle highlight in assuming all letters are  wide.

# Example
 

# The heights are  and . The tallest letter is  high and there are  letters. The hightlighted area will be  so the answer is.

# Function Description

# Complete the designerPdfViewer function in the editor below.

# designerPdfViewer has the following parameter(s):

# int h[26]: the heights of each letter
# string word: a string
# Returns

# int: the size of the highlighted area

import string

def designerPdfViewer(h, word):
    alphabets = list(string.ascii_lowercase)
    characters = list(word)
    character_heights = []
    #
    if(len(alphabets) == len(h)):
        for i in range(len(characters)):
            # print(h[alphabets.index(characters[i])])
            character_heights.append(h[alphabets.index(characters[i])])
            # break
    return max(character_heights) * len(word)
            

print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5], 'torn'))