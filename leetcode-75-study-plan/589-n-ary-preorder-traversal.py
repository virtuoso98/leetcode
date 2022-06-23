from collections import deque

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        if not root:
            return output
        
        stk = [root]
        while stk:
            node = stk.pop()
            output.append(node.val)
            for child in reversed(node.children):
                stk.append(child)
        return output