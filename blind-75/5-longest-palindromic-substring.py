class Solution:
    def longestPalindromeAux(self, s: str, ptrs: tuple[int, int], curr_max: tuple[int, int]) -> tuple[int, int]:
        l, r = ptrs
        curr_max_len = curr_max[1]-curr_max[0]+1
        while l >= 0 and r < len(s):
            if s[r] == s[l]:
                curr_len = r - l + 1
                if curr_len > curr_max_len:
                    curr_max_len = curr_len
                    curr_max = (l, r)
                r += 1; l -= 1
            else:
                break
        return curr_max

    def longestPalindrome(self, s: str) -> str:
        ans = (0, 0)
        for i in  range(len(s)): 
            ans = self.longestPalindromeAux(s, (i, i), ans)
            ans = self.longestPalindromeAux(s, (i, i+1), ans)
        return s[ans[0]:ans[1]+1]
        