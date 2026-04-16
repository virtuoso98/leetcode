class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ori = x
        rev = 0
        while x:
            rev *= 10
            rev += x % 10
            x //= 10

        return ori == rev