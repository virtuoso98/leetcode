# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Denoting left, right pointers
        l = 1
        r = n
        while l < r:
            m = l + (r - l) // 2
            # Trying to find first bad version
            if isBadVersion(m):
                r = m
            # Bad version not found yet
            else:
                l = m + 1
        return r