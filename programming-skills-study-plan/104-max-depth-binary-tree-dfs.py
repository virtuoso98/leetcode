class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Return max of left and right subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))