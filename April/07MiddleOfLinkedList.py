# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowp=head
        fastp=head
        if(head):
            while(fastp!=None and fastp.next!=None):
                slowp=slowp.next
                fastp=fastp.next.next
        return slowp
    
    
  