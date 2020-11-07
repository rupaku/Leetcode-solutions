'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''

# Solution::::::::::::::::::::::
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        counts= collections.Counter(s)
        max_freq = max(counts.values())
        buckets = [[] for _ in range(max_freq+1)]
        
        for c,i in counts.items():
            buckets[i].append(c)
            
        string_builder=[]
        for i in range(len(buckets)-1,0,-1):
            for c in buckets[i]:
                string_builder.append(c*i)
        return "".join(string_builder)
        
        