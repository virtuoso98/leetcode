class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        t = n
        sum_t = 0
        prod_t = 1
        while n != 0:
            sum_t += n % 10
            prod_t *= n % 10
            n //= 10
        return prod_t - sum_t