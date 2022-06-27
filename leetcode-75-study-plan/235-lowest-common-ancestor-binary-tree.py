class Solution:
    
    def lowestCommonAncestorAux(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # node exceeds range of p and q
        if node.val > q.val:
            return self.lowestCommonAncestor(node.left, p, q)
        
        # node below the range of p and q. Need to go higher
        elif node.val < p.val:
            return self.lowestCommonAncestor(node.right, p, q)
        
        # Divergence happens here
        else:
            return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Ensure p.val always smaller than q for lesser comparisons
        if p.val > q.val:
            return self.lowestCommonAncestorAux(root, q, p)
        # p value already below q
        return self.lowestCommonAncestorAux(root, p, q)