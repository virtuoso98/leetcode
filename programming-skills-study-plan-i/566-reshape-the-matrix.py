class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # Do not modify if dimensions same or illegal reshaping
        if m * n != r * c  or (m == r and n == c):
            return mat
        
        # Initialize new matrix to output
        out = [[None for _ in range(c)] for _ in range(r)]
        for i in range(m * n):
            out[i // c][i % c] = mat[i // n][i % n]
            
        return out