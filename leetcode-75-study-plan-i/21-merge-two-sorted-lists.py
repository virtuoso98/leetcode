class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive implementation"""
        
        if l2 is None:
            return l1
        
        elif l1 is None:
            return l2
        
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
            
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2