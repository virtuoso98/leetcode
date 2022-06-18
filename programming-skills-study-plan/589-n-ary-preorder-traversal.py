class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Pre-order, left to right means DFS.
        if root is None:
            return []
        # Stack is the best structure for this
        output = []
        s = [root]
        while s:
            node = s.pop()
            output.append(node.val)
            for child in reversed(node.children):
                s.append(child)
        return output