'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Solution::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy_head=ListNode()
        curr = head
        while curr:
            prev_p = dummy_head
            next_p = dummy_head.next
            while next_p:
                if curr.val < next_p.val:
                    break
                prev_p=prev_p.next
                next_p=next_p.next
            temp = curr.next
            curr.next=next_p
            prev_p.next= curr
            curr = temp
            
        return dummy_head.next
        