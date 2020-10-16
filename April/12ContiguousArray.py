
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen=0
        n=len(nums)
        for i in range(n):
            zero_count=0
            ones_count=0
            for j in range(i,n):
                if nums[j] == 0:
                    zero_count +=1
                else:
                    ones_count +=1
                if zero_count == ones_count:
                    maxlen = max(maxlen, j - i + 1)
            return maxlen
        