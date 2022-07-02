class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # reverse so that ones appear first
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]
        res = 0
        
        for i1, d1 in enumerate(num1_rev):
            for i2, d2 in enumerate(num2_rev):
                # Multiplication like in middle school
                res += int(d1) * int(d2) * 10 ** (i1 + i2)
                
        return str(res)