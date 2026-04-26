class Solution:
    def countSubStringsAux(self, s: str, l: int, r: int) -> int:
        cnt = 0
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return cnt
            cnt += 1; l -= 1; r += 1
        return cnt

    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            cnt += self.countSubStringsAux(s, i, i+1)
            cnt += self.countSubStringsAux(s, i, i)
        return cnt