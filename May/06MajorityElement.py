class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        for i in nums:
            if count[i] > len(nums)//2:
                return i
            
        