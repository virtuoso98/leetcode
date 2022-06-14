class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prehead = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            else:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next

        dummy.next = l1 if l1 else l2
        return prehead.next
