class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return 1
        while(len(stones) > 1):
            stones.sort()
            mx=stones[-1]
            sec_mx=stones[-2]
            if sec_mx == mx:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones.pop(-1)
                mx=abs(mx-sec_mx)
                stones[-1]= mx
        if(len(stones)):
            return stones[-1]
        return 0
        
        