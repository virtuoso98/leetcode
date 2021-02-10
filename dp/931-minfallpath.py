class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def min_array(arr):
            out = float('inf')
            for i in range(len(arr)):
                out = min(arr[i], out)
            return out

        row = len(matrix)
        col = len(matrix[0])
        # corner cases
        if row == 1:
            return min_array(matrix[0])

        if col == 1:
            acc = 0
            for i in range(row):
                acc += matrix[i][0]
            return acc

        # proceed to dp
        for i in range(1, row):
            matrix[i][0] += min(matrix[i - 1][0], matrix[i - 1][1])
            matrix[i][col - 1] += min(matrix[i - 1][col - 1], matrix[i - 1][col - 2])
            for j in range(1, col - 1):
                matrix[i][j] += min(matrix[i - 1][j], min(matrix[i - 1][j - 1],matrix[i - 1][j + 1]))


        return min_array(matrix[row - 1])