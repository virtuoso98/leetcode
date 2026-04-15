class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bits = 0
        while n:
            n_bits += n & 1
            n >>= 1
        return n_bits