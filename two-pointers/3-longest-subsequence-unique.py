class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        table = {}
        left = 0
        curr = 0
        for i in range(len(s)):
            if s[i] not in table:
                table[s[i]] = i
            elif left > table[s[i]]:
                table[s[i]] = i
            else:
                left = table[s[i]] + 1
                table[s[i]] = i
            curr = max(curr, i - left + 1)
            
        return curr
                