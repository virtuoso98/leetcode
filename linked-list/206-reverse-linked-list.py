# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next # store
            curr.next = prev # reverse step 1
            prev = curr # reverse step 2
            curr = next_node # traverse next
        
        return prev
            