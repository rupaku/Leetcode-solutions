'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
'''

# Solution::::::::::::::::::::::
from collections import Counter 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=collections.Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
        
        