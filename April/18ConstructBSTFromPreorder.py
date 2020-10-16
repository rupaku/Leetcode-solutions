# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root= TreeNode(preorder[0])
        stack=[root]
        for i in preorder[1:]:
            i=TreeNode(i)
            if i.val < stack[-1].val:
                stack[-1].left=i
                stack.append(i)
            else:
                while stack and stack[-1].val < i.val:
                    last=stack.pop(-1)
                last.right=i
                stack.append(i)
        return root
          