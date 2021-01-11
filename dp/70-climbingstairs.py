class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        # basically fibonacci sequence
        if n < 3 :
            return n
        else :
            arr = [1, 2]
            for i in range(3, n + 1):
                arr.append(arr[i - 2] + arr[i - 3])
            
            return arr[n - 1]