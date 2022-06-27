class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # if s repeats, then can find its subsequence like this
        return s in (s * 2)[1: -1]