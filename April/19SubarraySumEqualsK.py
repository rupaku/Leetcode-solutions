from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevSum = defaultdict(lambda : 0)
        n=len(nums)
        res = 0
        currsum = 0

        for i in range(0, n):  
            currsum += nums[i] 
            if currsum == k:  
                res += 1        

            if (currsum - k) in prevSum:
                res += prevSum[currsum - k] 

            prevSum[currsum] += 1

        return res 
