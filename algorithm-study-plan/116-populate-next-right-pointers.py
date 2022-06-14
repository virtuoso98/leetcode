"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Null case possible.
        if not root:
            return root

        # Use bfs to sequentially append nodes
        s = deque()
        s.append(root)
        while s:
            n = len(s)
            for i in range(n):
                node = s.popleft()
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
                # Rightmost node should not be appended
                if i < n - 1:
                    node.next = s[0]

        return root