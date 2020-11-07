'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
# Solution::::::::::::::::::::::
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len=len(s)
        p_len=len(p)
        if s_len < p_len:
            return []
        p_hash=Counter(p)
        s_hash=Counter() #empty hash
        output=[]
        for i in range(s_len):
            s_hash[s[i]] +=1
            #remove left letter from window
            if i >= p_len:
                if s_hash[s[i-p_len]] == 1:
                    del s_hash[s[i-p_len]]
                else:
                    s_hash[s[i-p_len]] -=1
            #compare both window
            if p_hash == s_hash:
                output.append(i-p_len+1)
        return output
        