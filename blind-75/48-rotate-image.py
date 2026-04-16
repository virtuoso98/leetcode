class Solution:
    def transpose(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, matrix: List[List[int]]) -> None:
        # reverse vertically
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[j][i], matrix[n-1-j][i] = matrix[n-1-j][i],matrix[j][i]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.reverse(matrix)
        self.transpose(matrix)
        return matrix