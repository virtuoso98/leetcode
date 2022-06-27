class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        first, second = 0, 1
        for _ in range(n - 1):
            tmp = second
            second = first + second
            first = tmp
        
        return second