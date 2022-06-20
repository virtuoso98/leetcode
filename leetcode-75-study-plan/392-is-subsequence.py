class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """2 Pointers Implementation"""
        if len(s) > len(t):
            return False
        
        s_len, t_len = len(s), len(t)
        # declare pointer
        s_ptr, t_ptr = 0, 0
        
        while s_ptr < len(s) and j < len(t_ptr):
            if s[s_ptr] == t[j]:
                s_ptr += 1
            t_ptr += 1
        
        # return True if s_ptr traverses through all of s
        return s_ptr == len(s)