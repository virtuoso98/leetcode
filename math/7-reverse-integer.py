class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31 - 1 or x == 0:
            return 0
        
        acc = 0
        if x > 0:
            isNeg = False
        else:
            isNeg = True
            x = -x
            
        
        while x != 0:
            acc *= 10
            acc += x % 10
            x = x // 10
    
        final = -acc if isNeg else acc
        return 0 if final > 2**31 - 1 or final < -2**31 else final
        