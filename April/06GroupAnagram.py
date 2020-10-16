class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            x="".join(sorted(i))
            if x in res:
                res[x].append(i)
            else:
                res[x]=[i]
                
        return list(res.values())
        