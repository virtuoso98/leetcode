# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        while n >= 0:
            n -= 1
            first = first.next
        
        while first:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return dummy.next