from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        r, c = len(grid), len(grid[0])
        n_fresh = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    n_fresh += 1

        # No rotting process required if no fresh oranges
        if n_fresh == 0: return 0

        # bfs for rotting oranges
        time = -1
        direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in direction:
                    new_x = dx + x
                    new_y = dy + y
                    if 0 <= new_x < r and 0 <= new_y < c and \
                    grid[new_x][new_y] == 1:
                        n_fresh -= 1
                        grid[new_x][new_y] = 2
                        q.append([new_x, new_y])
            time += 1

        return time if n_fresh == 0 else -1