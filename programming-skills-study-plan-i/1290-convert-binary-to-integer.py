class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        output = 0
        curr = head
        while curr:
            # Increase power by 2, since binary.
            # Bitwise operator saves the day here
            output <<= 1
            output += curr.val
            curr = curr.next
        return output
        