class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            else:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
        dummy.next = list1 if list1 else list2
        return dummy_head.next