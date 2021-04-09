class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans, exp = 0, 31
        while n:
            ans += (n & 1) << exp
            exp -= 1
            n >>= 1
        return ans