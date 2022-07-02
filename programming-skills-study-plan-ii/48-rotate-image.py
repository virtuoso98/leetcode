class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Brain not big enough to do rotation"""
        l = len(matrix)
        
        # Do transpose first
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Then reverse horizontally
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][l - j - 1] = matrix[i][l - j - 1], matrix[i][j]