class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        base_index = 0
        sl = len(s)
        tl = len(t)
        traverse = 0
        while traverse < tl :
            if base_index == sl :
                break
            else:
                if s[base_index] == t[traverse]:
                    base_index += 1 
                traverse += 1
        return base_index == sl