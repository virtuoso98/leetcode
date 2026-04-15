class Solution:
    def invertTreeAux(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTreeAux(root.left)
        self.invertTreeAux(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeAux(root)
        return root