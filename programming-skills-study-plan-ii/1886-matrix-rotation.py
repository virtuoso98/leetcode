class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        
        # Do transpose first
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Then reverse horizontally
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][l - j - 1] = matrix[i][l - j - 1], matrix[i][j]
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n_rotations = 0
        # At most 3 rotations are required
        while n_rotations <= 3:
            if mat == target:
                return True
            self.rotate(mat)
            n_rotations += 1
            
        return False