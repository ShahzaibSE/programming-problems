# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:

    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        for i in range(len(s)):
            ans = 0
            for i in range(len(s)-1, -1, -1):
                num = roman[s[i]]
                if(4*num < ans): 
                    ans -= num
                else:
                    ans += num
        return ans

s = Solution()
print('Test Case : 1')
s.romanToInt("III")
print('Test Case : 2')
s.romanToInt('LVIII')
print('Test Case : 3')
s.romanToInt('MCMXCIV')