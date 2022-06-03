from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        while q:
            x, y = q.popleft()
            # I really don't understand how not creating a new direction
            # array doesn't work but this will have to do.
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= new_x < len(mat) and 0 <= new_y < len(mat[0]) \
                and (new_x, new_y) not in visited:
                    q.append([new_x, new_y])
                    visited.add((new_x, new_y))
                    mat[new_x][new_y] = mat[x][y] + 1

        return mat
