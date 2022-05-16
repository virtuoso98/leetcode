class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        l = 0
        for i in range(len(s)):
            c = s[i]
            # Left pointer to track last seen char
            if c in d:
                l = max(d[c] + 1, l)
            d[c] = i
            ans = max(i - l + 1, ans)
            
        return ans