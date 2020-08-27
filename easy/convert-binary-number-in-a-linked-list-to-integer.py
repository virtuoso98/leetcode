class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        count = -1 
        count_list = head
        iterate_list = head
        acc = 0
        
        while count_list:
            count += 1
            count_list = count_list.next
        
        while iterate_list:
            acc += iterate_list.val * (2 ** count)
            count -= 1
            iterate_list = iterate_list.next
            
        return acc

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

    