class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        
        # Perform Transpose
        for i in range(l):
            for j in range(i, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        print(matrix)
        
        # Perform reversal
        for i in range(l):
            for j in range(l // 2):
                matrix[i][j], matrix[i][l - 1 - j] = matrix[i][l - 1 - j], matrix[i][j]