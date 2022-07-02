class Solution:
    def isValidBSTAux(self, node, floor, ceil):
        if not node:
            return True
        
        if floor >= node.val or ceil <= node.val:
            return False
        
        isLeftValidBST = self.isValidBSTAux(node.left, floor, node.val)
        isRightValidBST = self.isValidBSTAux(node.right, node.val, ceil)
        
        return isLeftValidBST and isRightValidBST   
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid_bst = self.isValidBSTAux(root, float('-inf'), float('inf'))
        return is_valid_bst