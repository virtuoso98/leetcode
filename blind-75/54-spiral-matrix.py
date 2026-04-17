class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        x, y, dir_ptr = 0, 0, 0
        l, w = len(matrix[0]), len(matrix)
        n = l * w
        x_lb, x_ub, y_lb, y_ub = 0, l, 0, w
        output = []
        while n > 0:
            output.append(matrix[y][x])
            dx, dy = direction[dir_ptr]
            is_dir_change = False
            if x + dx < x_lb: 
                is_dir_change = True
                y_ub -= 1
            elif x + dx >= x_ub:
                is_dir_change = True
                y_lb += 1
            elif y + dy < y_lb:
                is_dir_change = True
                x_lb += 1
            elif y + dy >= y_ub:
                is_dir_change = True
                x_ub -= 1

            if is_dir_change:
                dir_ptr = (dir_ptr + 1) % len(direction)
                dx, dy = direction[dir_ptr]
            x, y = x + dx, y + dy
            n -= 1
        return output
