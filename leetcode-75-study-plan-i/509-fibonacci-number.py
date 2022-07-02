class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0, 1]
        for _ in range(n - 1):
            dp.append(dp[-1] + dp[-2])
            
        return dp[-1]
        