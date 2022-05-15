# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Insert Dummy Node. Very Important Trick!
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        # Removing n-th node from end, so 0-index to compensate
        while n >= 0:
            fast = fast.next
            n -= 1
            
        # Move slow pointer to figure out which node to remove
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next