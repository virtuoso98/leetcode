class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        acc = None  
        
        # putting None removes reference
        
        while head:
            temp = head.next  
            head.next = acc
            acc = head
            head = temp
        
        return acc