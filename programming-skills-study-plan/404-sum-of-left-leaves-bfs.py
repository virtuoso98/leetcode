from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, False)])
        total = 0
        while q:
            node, is_left = q.popleft()
            # If left leave, add to total
            if not node.right and not node.left and is_left:
                total += node.val
            # Append, along with a flag saying whether it is left subtree
            if node.left:
                q.append((node.left, True))
            if node.right:
                q.append((node.right, False))
        return total