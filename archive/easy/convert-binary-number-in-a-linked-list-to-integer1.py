class Solution(object):

    def getDecimalValue_v1(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        val = head.val
        head = head.next
        
        while head:
            val = val << 1 
            val += head.val
            head = head.next
            
        return val