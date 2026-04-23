class Solution:
    def isValidBSTAux(self, root: Optional[TreeNode], lower, upper) -> bool:
        if root is None:
            return True
        if lower >= root.val or upper <= root.val:
            return False
        return self.isValidBSTAux(root.left, lower, root.val) and self.isValidBSTAux(root.right, root.val, upper)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTAux(root, float("-inf"), float("inf"))