'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
'''
# Solution::::::::::::::::::::::
class Solution:
    def checkInclusion(self, s1, s2):
        count_map_s1 = collections.Counter(s1)
        count_map_s2 = collections.Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if count_map_s1 == count_map_s2:
                return True

            count_map_s2[s2[i]] += 1
            count_map_s2[s2[i - len(s1)]] -= 1
            if count_map_s2[s2[i - len(s1)]] == 0:
                del(count_map_s2[s2[i - len(s1)]])

        return count_map_s2 == count_map_s1