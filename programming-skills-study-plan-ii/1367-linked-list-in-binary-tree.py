class Solution:
    def isSubPathAux(self, target, node, path) -> bool:
        if target in path:
            return True
        
        if not node:
            return False
    
        is_right_subpath = self.isSubPathAux(target, node.right, f"{path}{node.val}")
        is_left_subpath = self.isSubPathAux(target, node.left, f"{path}{node.val}")
        return is_right_subpath or is_left_subpath
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Convert target to immutable string so less problems with object reference
        target_arr = []
        while head:
            target_arr.append(str(head.val))
            head = head.next
            
        target = "".join(target_arr)
        return self.isSubPathAux(target, root, "")