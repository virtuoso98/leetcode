class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        n_bits_remaining = 32
        while n_bits_remaining:
            res = (res << 1) | (n & 1)
            n >>= 1
            n_bits_remaining -= 1
        return res