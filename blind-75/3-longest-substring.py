class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, n = 0, 0, len(s)
        ans = 0
        char_idx = dict()
        while r < n:
            c = s[r]
            if c in char_idx.keys():
                last_idx = char_idx[c]
                if l <= last_idx:
                    l = last_idx + 1
            char_idx[c] = r
            ans = max(ans, r - l + 1) 
            r += 1
        return ans
