class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = dict()
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        
        max_len = 0
        for v in count.values():
            # Round down to nearest even letters
            max_len += v - v % 2
            # If max_len is even and v is odd,
            # can slot 1 letter in the middle
            if max_len % 2 == 0 and v % 2 == 1:
                max_len += 1
                
        return max_len