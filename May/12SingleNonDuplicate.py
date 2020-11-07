'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
'''

# Solution::::::::::::::::::::::
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while(l < h):
            mid=l+(h-l)//2
            if mid % 2 == 1:
                mid=mid-1
            #we want only even index
            if nums[mid] == nums[mid+1]:
                l=mid+2
            else:
                h=mid
        return nums[l]
        