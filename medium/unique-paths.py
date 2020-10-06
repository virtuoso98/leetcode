class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1 :
            return 1
        
        def fac(n):    
            if n == 1:
                return 1
            else:
                return n * fac(n - 1)
        
        total_ways = fac(m + n - 2)
        right_permute = fac(n - 1)
        left_permute = fac(m - 1)
        
        return (total_ways//(right_permute * left_permute))