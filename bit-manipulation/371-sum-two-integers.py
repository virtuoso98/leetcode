class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        
        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1
        
        if (a * b >= 0):
            while y:
                ans, carry = x ^ y, (x & y) << 1
                x, y = ans, carry

        else:
            while y:
                ans, carry = x ^ y, ((~x) & y) << 1
                x, y = ans, carry
        
        return x * sign