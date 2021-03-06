# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # placeholder pointer
        curr = ListNode(0)
        dummy = curr
        
        while l1 and l2:
            if (l1.val <= l2.val):
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            # Important!! Update dummy to next point
            dummy = dummy.next
                
        if l1 != None:
            dummy.next = l1
            
        else:
            dummy.next = l2
        
        return curr.next