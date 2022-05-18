class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stk = [(sr, sc)]
        srcColor = image[sr][sc]
        visited = set()
        while stk:
            r, c = stk.pop()
            # Remember to add visited
            if image[r][c] == srcColor and (r, c) not in visited:
                image[r][c] = newColor
                if r > 0:
                    stk.append((r - 1, c))
                if r < len(image) - 1:
                    stk.append((r + 1, c))
                if c > 0:
                    stk.append((r, c - 1))
                if c < len(image[0]) - 1:
                    stk.append((r, c + 1))
            visited.add((r, c))

        return image
