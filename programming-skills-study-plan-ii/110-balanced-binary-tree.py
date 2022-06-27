class Solution:
    def treeHeight(self, node: Optional[TreeNode]) -> int:
        """Helper to calculate tree height"""
        if not node:
            return 0
        left_subtree_height = self.treeHeight(node.left)
        right_subtree_height = self.treeHeight(node.right)    
        return 1 + max(left_subtree_height, right_subtree_height)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # If their heights differ by more than 1, return False
        if abs(self.treeHeight(root.left) - self.treeHeight(root.right)) > 1:
            return False
        
        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)
        
        # Return True only if ALL subtrees are balanced
        return is_left_balanced and is_right_balanced