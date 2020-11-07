'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
'''

# Solution::::::::::::::::::::::
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(r):
            return inorder(r.left)+[r.val]+inorder(r.right) if r else []
        return inorder(root)[k-1]
        