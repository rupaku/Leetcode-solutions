'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
'''

# Solution::::::::::::::::::::::
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
