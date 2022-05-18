class Solution:
    def bfs(self, i, j, grid, R, C) -> int:
        stk = [(i, j)]
        area = 0
        while stk:
            r, c = stk.pop()
            if grid[r][c] == 1:
                grid[r][c] = 0
                area += 1
                if r > 0:
                    stk.append((r - 1, c))
                if r < R - 1:
                    stk.append((r + 1, c))
                if c > 0:
                    stk.append((r, c - 1))
                if c < C - 1:
                    stk.append((r, c + 1))
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Don't need visited set because overwriting occurs
        R, C = len(grid), len(grid[0])
        max_area = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    area = self.bfs(i, j, grid, R, C)
                    max_area = max(max_area, area)
        return max_area