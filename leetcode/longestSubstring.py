# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = [0] * 26
        print(visited)
        for char in s:
            print(char)

sol = Solution()
sol.lengthOfLongestSubstring('pwwkew')