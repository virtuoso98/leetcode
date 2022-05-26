class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # The explanation... is just math
        # power of 2: only 1 bit at the left
        return n & (n - 1) == 0 and n > 0
        