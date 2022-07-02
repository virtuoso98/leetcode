class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        curr_dir = 0
        x, y = 0, 0
        n_elements_left = R * C
        res = []
        
        while n_elements_left != 0:
            # Append result and mark as visited
            res.append(matrix[y][x])
            matrix[y][x] = None
            n_elements_left -= 1
            
            # Whether to change direction or not
            dx, dy = direction[curr_dir]
            
            new_x, new_y = x + dx, y + dy
            # to maintain direction, x, y must be in bounds
            # and next x, y has not been visited before
            if 0 <= new_x < C and 0 <= new_y < R and matrix[new_y][new_x] is not None:
                x, y = new_x, new_y
                
            else:
                curr_dir = (curr_dir + 1) % 4
                dx, dy = direction[curr_dir]
                x, y = x + dx, y + dy
        
        return res