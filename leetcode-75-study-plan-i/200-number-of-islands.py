class Solution:
    def removeIsland(self, grid: List[List[str]], i: int, j: int) -> None:
        area = 0
        stk = [(i, j)]
        R, C = len(grid), len(grid[0])
        
        while stk:
            r, c = stk.pop()
            if grid[r][c] == "1":
                grid[r][c] = "0"
                if r - 1 >= 0: stk.append((r - 1, c))
                if r + 1 < R: stk.append((r + 1, c))
                if c - 1 >= 0: stk.append((r, c - 1))
                if c + 1 < C: stk.append((r, c + 1))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # No changes if pixel already in new colour:
        n_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    n_islands += 1
                    self.removeIsland(grid, i, j)
                    
        return n_islands