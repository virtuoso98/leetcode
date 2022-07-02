class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Alternatively, can use floyd tortoise and hare algo"""
        seen = set()
        curr = head
        while curr:
            # Set storing references
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next
        return None