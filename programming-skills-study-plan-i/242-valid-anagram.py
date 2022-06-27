class Solution:
    def updateVal(self, c: str, char_diff: dict, is_t: bool) -> None:
        # Check differences in character count
        if c not in char_diff:
            char_diff[c] = -1 if is_t else 1
        else:
            char_diff[c] += -1 if is_t else 1
    
    def isAnagram(self, s: str, t: str) -> bool:
        # If length unequal, impossible to be anagram
        if len(s) != len(t):
            return False
        
        char_diff = dict()
        for i in range(len(s)):
            self.updateVal(s[i], char_diff, is_t = False)
            self.updateVal(t[i], char_diff, is_t = True)
            
        for diff in char_diff.values():
            if diff != 0:
                return False
            
        return True