# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        acc = 0
        while head:
            acc *= 2 
            acc += head.val
            head = head.next
        
        return acc
            