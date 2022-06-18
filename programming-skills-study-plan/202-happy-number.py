class Solution:
    def processNum(self, n: int) -> int:
        new_num = 0
        while n != 0:
            new_num += (n % 10) ** 2
            n //= 10
        return new_num

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            n = self.processNum(n)
            if n in seen:
                return False
        return True